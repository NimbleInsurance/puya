from collections.abc import Iterator, Mapping

import mypy.nodes
import mypy.types
import mypy.visitor

from puya import log
from puya.awst.nodes import (
    ContractFragment,
    ContractMethod,
)
from puya.awst_build import constants, pytypes
from puya.awst_build.arc4_utils import get_arc4_abimethod_data, get_arc4_baremethod_data
from puya.awst_build.base_mypy_visitor import BaseMyPyStatementVisitor
from puya.awst_build.context import ASTConversionModuleContext
from puya.awst_build.contract_data import AppStorageDeclaration, ContractClassOptions
from puya.awst_build.subroutine import ContractMethodInfo, FunctionASTConverter
from puya.awst_build.utils import (
    get_decorators_by_fullname,
    iterate_user_bases,
    qualified_class_name,
)
from puya.errors import CodeError, InternalError
from puya.models import (
    ARC4MethodConfig,
    ContractReference,
    OnCompletionAction,
)
from puya.parse import SourceLocation
from puya.utils import unique

ALLOWABLE_OCA = frozenset(
    [oca.name for oca in OnCompletionAction if oca != OnCompletionAction.ClearState]
)

logger = log.get_logger(__name__)


class ContractASTConverter(BaseMyPyStatementVisitor[None]):
    def __init__(
        self,
        context: ASTConversionModuleContext,
        class_def: mypy.nodes.ClassDef,
        class_options: ContractClassOptions,
    ):
        super().__init__(context=context)
        self.class_def = class_def
        self.cref = qualified_class_name(class_def.info)
        self._is_arc4 = class_def.info.has_base(constants.ARC4_CONTRACT_BASE)
        self._is_abstract = _check_class_abstractness(context, class_def)
        self._approval_program: ContractMethod | None = None
        self._clear_program: ContractMethod | None = None
        self._init_method: ContractMethod | None = None
        self._subroutines = list[ContractMethod]()
        inherited_and_direct_storage = _gather_app_storage_recursive(context, class_def)
        self.context.set_state_defs(self.cref, inherited_and_direct_storage)

        # if the class has an __init__ method, we need to visit it first, so any storage
        # fields cane be resolved to a (static) key
        match class_def.info.names.get("__init__"):
            case mypy.nodes.SymbolTableNode(node=mypy.nodes.Statement() as init_node):
                stmts = unique((init_node, *class_def.defs.body))
            case _:
                stmts = class_def.defs.body
        # note: we iterate directly and catch+log code errors here,
        #       since each statement should be somewhat independent given
        #       the constraints we place (e.g. if one function fails to convert,
        #       we can still keep trying to convert other functions to produce more valid errors)
        for stmt in stmts:
            with context.log_exceptions(fallback_location=stmt):
                stmt.accept(self)
        # TODO: validation for state proxies being non-conditional

        app_state = {
            name: state_decl.definition
            for name, state_decl in context.state_defs(self.cref).items()
            if state_decl.defined_in == self.cref
        }

        self.result_ = ContractFragment(
            module_name=self.cref.module_name,
            name=self.cref.class_name,
            name_override=class_options.name_override,
            is_arc4=self._is_arc4,
            is_abstract=self._is_abstract,
            bases=_gather_bases(context, class_def),
            init=self._init_method,
            approval_program=self._approval_program,
            clear_program=self._clear_program,
            subroutines=self._subroutines,
            app_state=app_state,
            docstring=class_def.docstring,
            source_location=self._location(class_def),
            reserved_scratch_space=class_options.scratch_slot_reservations,
            state_totals=class_options.state_totals,
        )

    @classmethod
    def convert(
        cls,
        context: ASTConversionModuleContext,
        class_def: mypy.nodes.ClassDef,
        class_options: ContractClassOptions,
    ) -> ContractFragment:
        return cls(context, class_def, class_options).result_

    def empty_statement(self, _stmt: mypy.nodes.Statement) -> None:
        return None

    def visit_function(
        self,
        func_def: mypy.nodes.FuncDef,
        decorator: mypy.nodes.Decorator | None,
    ) -> None:
        func_loc = self._location(func_def)
        self._precondition(
            self._is_abstract or func_def.abstract_status == mypy.nodes.NOT_ABSTRACT,
            "class abstract method(s) but was not detected as abstract by mypy",
            func_loc,
        )
        source_location = self._location(decorator or func_def)

        keep_going = True
        if func_def.is_class:
            self._error("@classmethod not supported", func_loc)
            keep_going = False
        if func_def.is_static:
            self._error(
                "@staticmethod not supported, use a module level function instead", func_loc
            )
            keep_going = False

        dec_by_fullname = get_decorators_by_fullname(self.context, decorator) if decorator else {}
        # TODO: validate decorator ordering?
        dec_by_fullname.pop("abc.abstractmethod", None)
        for unknown_dec_fullname in dec_by_fullname.keys() - frozenset(
            constants.KNOWN_METHOD_DECORATORS
        ):
            dec = dec_by_fullname.pop(unknown_dec_fullname)
            self._error(f'Unsupported decorator "{unknown_dec_fullname}"', dec)

        if not keep_going:
            pass  # unrecoverable error in prior validation,
        # TODO: handle difference of subroutine vs abimethod and overrides???
        elif func_def.name == "__init__":
            sub = self._handle_method(
                func_def,
                extra_decorators=dec_by_fullname,
                arc4_method_config=None,
                source_location=source_location,
            )
            if sub is not None:
                self._init_method = sub
        elif func_def.name.startswith("__") and func_def.name.endswith("__"):
            self._error(
                "methods starting and ending with a double underscore"
                ' (aka "dunder" methods) are reserved for the Python data model'
                " (https://docs.python.org/3/reference/datamodel.html)."
                " Of these methods, only __init__ is supported in contract classes",
                func_loc,
            )
        elif (
            is_approval := func_def.name == constants.APPROVAL_METHOD
        ) or func_def.name == constants.CLEAR_STATE_METHOD:
            sub = self._handle_method(
                func_def,
                extra_decorators=dec_by_fullname,
                arc4_method_config=None,
                source_location=source_location,
            )
            if sub is not None:
                if is_approval:
                    self._approval_program = sub
                else:
                    self._clear_program = sub
        elif not self._is_arc4:
            for arc4_only_dec_name in (
                constants.ABIMETHOD_DECORATOR,
                constants.BAREMETHOD_DECORATOR,
            ):
                if invalid_dec := dec_by_fullname.pop(arc4_only_dec_name, None):
                    self._error(
                        f"decorator is only valid in subclasses of"
                        f" {pytypes.ARC4ContractBaseType}",
                        invalid_dec,
                    )
            if not dec_by_fullname.pop(constants.SUBROUTINE_HINT, None):
                self._error(f"missing @{constants.SUBROUTINE_HINT_ALIAS} decorator", func_loc)
            sub = self._handle_method(
                func_def,
                extra_decorators=dec_by_fullname,
                arc4_method_config=None,
                source_location=source_location,
            )
            if sub is not None:
                self._subroutines.append(sub)
        else:
            subroutine_dec = dec_by_fullname.pop(constants.SUBROUTINE_HINT, None)
            abimethod_dec = dec_by_fullname.pop(constants.ABIMETHOD_DECORATOR, None)
            baremethod_dec = dec_by_fullname.pop(constants.BAREMETHOD_DECORATOR, None)

            if len(list(filter(None, (subroutine_dec, abimethod_dec, baremethod_dec)))) != 1:
                self._error(
                    f"ARC-4 contract member functions"
                    f" (other than __init__ or approval / clear program methods)"
                    f" must be annotated with exactly one of"
                    f" @{constants.SUBROUTINE_HINT_ALIAS},"
                    f" @{constants.ABIMETHOD_DECORATOR_ALIAS},"
                    f" or @{constants.BAREMETHOD_DECORATOR_ALIAS}",
                    func_loc,
                )

            arc4_method_config: ARC4MethodConfig | None
            if abimethod_dec:
                arc4_method_config = get_arc4_abimethod_data(
                    self.context, abimethod_dec, func_def
                ).config
            elif baremethod_dec:
                arc4_method_config = get_arc4_baremethod_data(
                    self.context, baremethod_dec, func_def
                )
            else:
                arc4_method_config = None
            # TODO: validate against super-class configs??
            sub = self._handle_method(
                func_def,
                extra_decorators=dec_by_fullname,
                arc4_method_config=arc4_method_config,
                source_location=source_location,
            )
            if sub is not None:
                self._subroutines.append(sub)

    def _handle_method(
        self,
        func_def: mypy.nodes.FuncDef,
        extra_decorators: Mapping[str, mypy.nodes.Expression],
        arc4_method_config: ARC4MethodConfig | None,
        source_location: SourceLocation,
    ) -> ContractMethod | None:
        func_loc = self._location(func_def)
        self._precondition(
            not (func_def.is_static or func_def.is_class),
            "only instance methods should have made it to this point",
            func_loc,
        )
        for dec_fullname, dec in extra_decorators.items():
            self._error(f'Unsupported decorator "{dec_fullname}"', dec)
        if len(func_def.arguments) < 1:
            # since we checked we're only handling instance methods, should be at least one
            # argument to function - ie self
            self._error(f"{func_def.name} should take a self parameter", func_loc)
        match func_def.abstract_status:
            case mypy.nodes.NOT_ABSTRACT:
                return FunctionASTConverter.convert(
                    self.context,
                    func_def=func_def,
                    source_location=source_location,
                    contract_method_info=ContractMethodInfo(
                        type_info=self.class_def.info,
                        arc4_method_config=arc4_method_config,
                        cref=self.cref,
                    ),
                )
            case mypy.nodes.IMPLICITLY_ABSTRACT:
                # TODO: should we have a placeholder item instead? need to handle via super() if so
                self.context.info(
                    f"Skipping (implicitly) abstract method {func_def.name}",
                    func_loc,
                )
                return None
            case mypy.nodes.IS_ABSTRACT:
                # TODO: should we have a placeholder item instead? need to handle via super() if so
                self.context.info(
                    f"Skipping abstract method {func_def.name}",
                    func_loc,
                )
                return None
            case _ as unknown_value:
                raise InternalError(
                    f"Unknown value for abstract_status: {unknown_value}", func_loc
                )

    def visit_block(self, o: mypy.nodes.Block) -> None:
        raise InternalError("shouldn't get here", self._location(o))

    def visit_return_stmt(self, stmt: mypy.nodes.ReturnStmt) -> None:
        self._error("illegal Python syntax, return in class body", location=stmt)

    def visit_class_def(self, cdef: mypy.nodes.ClassDef) -> None:
        self._error("nested classes are not supported", location=cdef)

    def _unsupported_stmt(self, kind: str, stmt: mypy.nodes.Statement) -> None:
        self._error(f"{kind} statements are not supported in the class body", location=stmt)

    def visit_assignment_stmt(self, stmt: mypy.nodes.AssignmentStmt) -> None:
        # just pass on state forward-declarations, these will be picked up by gather state
        # everything else (ie any _actual_ assignments) is unsupported
        if not isinstance(stmt.rvalue, mypy.nodes.TempNode):
            self._unsupported_stmt("assignment", stmt)

    def visit_operator_assignment_stmt(self, stmt: mypy.nodes.OperatorAssignmentStmt) -> None:
        self._unsupported_stmt("operator assignment", stmt)

    def visit_expression_stmt(self, stmt: mypy.nodes.ExpressionStmt) -> None:
        if isinstance(stmt.expr, mypy.nodes.StrExpr):
            # ignore class docstring, already extracted
            # TODO: should we capture field "docstrings"?
            pass
        else:
            self._unsupported_stmt("expression statement", stmt)

    def visit_if_stmt(self, stmt: mypy.nodes.IfStmt) -> None:
        self._unsupported_stmt("if", stmt)

    def visit_while_stmt(self, stmt: mypy.nodes.WhileStmt) -> None:
        self._unsupported_stmt("while", stmt)

    def visit_for_stmt(self, stmt: mypy.nodes.ForStmt) -> None:
        self._unsupported_stmt("for", stmt)

    def visit_break_stmt(self, stmt: mypy.nodes.BreakStmt) -> None:
        self._unsupported_stmt("break", stmt)

    def visit_continue_stmt(self, stmt: mypy.nodes.ContinueStmt) -> None:
        self._unsupported_stmt("continue", stmt)

    def visit_assert_stmt(self, stmt: mypy.nodes.AssertStmt) -> None:
        self._unsupported_stmt("assert", stmt)

    def visit_del_stmt(self, stmt: mypy.nodes.DelStmt) -> None:
        self._unsupported_stmt("del", stmt)

    def visit_match_stmt(self, stmt: mypy.nodes.MatchStmt) -> None:
        self._unsupported_stmt("match", stmt)


def _gather_bases(
    context: ASTConversionModuleContext, class_def: mypy.nodes.ClassDef
) -> list[ContractReference]:
    class_def_loc = context.node_location(class_def)
    contract_bases_mro = list[ContractReference]()
    for base_type in iterate_user_bases(class_def.info):
        base_cref = qualified_class_name(base_type)
        if "." in base_cref.class_name:
            raise CodeError(
                f"Reference to base class {base_type.fullname},"
                f" which is nested inside another class",
                class_def_loc,
            )

        try:
            base_symbol = context.parse_result.manager.modules[base_cref.module_name].names[
                base_cref.class_name
            ]
        except KeyError as ex:
            raise InternalError(
                f"Couldn't resolve reference to class {base_cref.class_name}"
                f" in module {base_cref.module_name}",
                class_def_loc,
            ) from ex
        base_class_info = base_symbol.node
        if not isinstance(base_class_info, mypy.nodes.TypeInfo):
            raise CodeError(
                f"Base class {base_type.fullname} is not a class,"
                f" node type is {type(base_class_info).__name__}",
                class_def_loc,
            )
        if not base_class_info.has_base(constants.CONTRACT_BASE):
            raise CodeError(
                f"Base class {base_type.fullname} is not a contract subclass", class_def_loc
            )
        contract_bases_mro.append(base_cref)

    return contract_bases_mro


def _gather_app_storage_recursive(
    context: ASTConversionModuleContext, class_def: mypy.nodes.ClassDef
) -> dict[str, AppStorageDeclaration]:
    this_global_directs = {
        defn.member_name: defn for defn in _gather_global_direct_storages(context, class_def.info)
    }
    combined_app_state = this_global_directs.copy()
    for base in iterate_user_bases(class_def.info):
        base_cref = qualified_class_name(base)
        base_app_state = {
            name: defn
            for name, defn in context.state_defs(base_cref).items()
            if defn.defined_in == base_cref
        }
        for redefined_member in combined_app_state.keys() & base_app_state.keys():
            # only handle producing errors for direct globals here,
            # proxies get handled on insert
            if this_member_redef := combined_app_state.get(redefined_member):
                member_orig = base_app_state[redefined_member]
                context.info(
                    f"Previous definition of {redefined_member} was here",
                    member_orig.source_location,
                )
                context.error(
                    f"Redefinition of {redefined_member}",
                    this_member_redef.source_location,
                )
        # we do it this way around so that we keep combined_app_state with the most-derived
        # definition in case of redefinitions
        combined_app_state = base_app_state | combined_app_state
    return combined_app_state


def _gather_global_direct_storages(
    context: ASTConversionModuleContext, class_info: mypy.nodes.TypeInfo
) -> Iterator[AppStorageDeclaration]:
    cref = qualified_class_name(class_info)
    for name, sym in class_info.names.items():
        if isinstance(sym.node, mypy.nodes.Var):
            var_loc = context.node_location(sym.node)
            if sym.type is None:
                raise InternalError(
                    f"symbol table for class {class_info.fullname}"
                    f" contains Var node entry for {name} without type",
                    var_loc,
                )
            pytyp = context.type_to_pytype(sym.type, source_location=var_loc)

            if isinstance(pytyp, pytypes.StorageProxyType | pytypes.StorageMapProxyType):
                # these are handled on declaration, need to collect constructor arguments too
                continue

            if pytyp is pytypes.NoneType:
                context.error("None is not supported as a value, only a return type", var_loc)
            yield AppStorageDeclaration(
                member_name=name,
                typ=pytyp,
                source_location=var_loc,
                defined_in=cref,
                key_override=None,
                description=None,
            )


def _check_class_abstractness(
    context: ASTConversionModuleContext, class_def: mypy.nodes.ClassDef
) -> bool:
    is_abstract = class_def.info.is_abstract
    # note: we don't support the metaclass= option, so we only need to check for
    # inheritance of abc.ABC and not  metaclass=abc.ABCMeta
    if is_abstract and not any(
        base.fullname == "abc.ABC" for base in class_def.info.direct_base_classes()
    ):
        context.warning(f"Class {class_def.fullname} is implicitly abstract", class_def)
    return is_abstract
