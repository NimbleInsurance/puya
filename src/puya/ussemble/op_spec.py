from puya.ussemble.op_spec_models import ImmediateEnum, ImmediateKind, OpSpec

OP_SPECS = {
    "err": OpSpec(name="err", code=0, immediates=[]),
    "sha256": OpSpec(name="sha256", code=1, immediates=[]),
    "keccak256": OpSpec(name="keccak256", code=2, immediates=[]),
    "sha512_256": OpSpec(name="sha512_256", code=3, immediates=[]),
    "ed25519verify": OpSpec(name="ed25519verify", code=4, immediates=[]),
    "ecdsa_verify": OpSpec(
        name="ecdsa_verify",
        code=5,
        immediates=[ImmediateEnum(codes={"Secp256k1": 0, "Secp256r1": 1})],
    ),
    "ecdsa_pk_decompress": OpSpec(
        name="ecdsa_pk_decompress",
        code=6,
        immediates=[ImmediateEnum(codes={"Secp256k1": 0, "Secp256r1": 1})],
    ),
    "ecdsa_pk_recover": OpSpec(
        name="ecdsa_pk_recover",
        code=7,
        immediates=[ImmediateEnum(codes={"Secp256k1": 0, "Secp256r1": 1})],
    ),
    "+": OpSpec(name="+", code=8, immediates=[]),
    "-": OpSpec(name="-", code=9, immediates=[]),
    "/": OpSpec(name="/", code=10, immediates=[]),
    "*": OpSpec(name="*", code=11, immediates=[]),
    "<": OpSpec(name="<", code=12, immediates=[]),
    ">": OpSpec(name=">", code=13, immediates=[]),
    "<=": OpSpec(name="<=", code=14, immediates=[]),
    ">=": OpSpec(name=">=", code=15, immediates=[]),
    "&&": OpSpec(name="&&", code=16, immediates=[]),
    "||": OpSpec(name="||", code=17, immediates=[]),
    "==": OpSpec(name="==", code=18, immediates=[]),
    "!=": OpSpec(name="!=", code=19, immediates=[]),
    "!": OpSpec(name="!", code=20, immediates=[]),
    "len": OpSpec(name="len", code=21, immediates=[]),
    "itob": OpSpec(name="itob", code=22, immediates=[]),
    "btoi": OpSpec(name="btoi", code=23, immediates=[]),
    "%": OpSpec(name="%", code=24, immediates=[]),
    "|": OpSpec(name="|", code=25, immediates=[]),
    "&": OpSpec(name="&", code=26, immediates=[]),
    "^": OpSpec(name="^", code=27, immediates=[]),
    "~": OpSpec(name="~", code=28, immediates=[]),
    "mulw": OpSpec(name="mulw", code=29, immediates=[]),
    "addw": OpSpec(name="addw", code=30, immediates=[]),
    "divmodw": OpSpec(name="divmodw", code=31, immediates=[]),
    "intcblock": OpSpec(name="intcblock", code=32, immediates=[ImmediateKind.varuint_array]),
    "intc": OpSpec(name="intc", code=33, immediates=[ImmediateKind.uint8]),
    "intc_0": OpSpec(name="intc_0", code=34, immediates=[]),
    "intc_1": OpSpec(name="intc_1", code=35, immediates=[]),
    "intc_2": OpSpec(name="intc_2", code=36, immediates=[]),
    "intc_3": OpSpec(name="intc_3", code=37, immediates=[]),
    "bytecblock": OpSpec(name="bytecblock", code=38, immediates=[ImmediateKind.bytes_array]),
    "bytec": OpSpec(name="bytec", code=39, immediates=[ImmediateKind.uint8]),
    "bytec_0": OpSpec(name="bytec_0", code=40, immediates=[]),
    "bytec_1": OpSpec(name="bytec_1", code=41, immediates=[]),
    "bytec_2": OpSpec(name="bytec_2", code=42, immediates=[]),
    "bytec_3": OpSpec(name="bytec_3", code=43, immediates=[]),
    "arg": OpSpec(name="arg", code=44, immediates=[ImmediateKind.uint8]),
    "arg_0": OpSpec(name="arg_0", code=45, immediates=[]),
    "arg_1": OpSpec(name="arg_1", code=46, immediates=[]),
    "arg_2": OpSpec(name="arg_2", code=47, immediates=[]),
    "arg_3": OpSpec(name="arg_3", code=48, immediates=[]),
    "txn": OpSpec(
        name="txn",
        code=49,
        immediates=[
            ImmediateEnum(
                codes={
                    "Sender": 0,
                    "Fee": 1,
                    "FirstValid": 2,
                    "FirstValidTime": 3,
                    "LastValid": 4,
                    "Note": 5,
                    "Lease": 6,
                    "Receiver": 7,
                    "Amount": 8,
                    "CloseRemainderTo": 9,
                    "VotePK": 10,
                    "SelectionPK": 11,
                    "VoteFirst": 12,
                    "VoteLast": 13,
                    "VoteKeyDilution": 14,
                    "Type": 15,
                    "TypeEnum": 16,
                    "XferAsset": 17,
                    "AssetAmount": 18,
                    "AssetSender": 19,
                    "AssetReceiver": 20,
                    "AssetCloseTo": 21,
                    "GroupIndex": 22,
                    "TxID": 23,
                    "ApplicationID": 24,
                    "OnCompletion": 25,
                    "ApplicationArgs": 26,
                    "NumAppArgs": 27,
                    "Accounts": 28,
                    "NumAccounts": 29,
                    "ApprovalProgram": 30,
                    "ClearStateProgram": 31,
                    "RekeyTo": 32,
                    "ConfigAsset": 33,
                    "ConfigAssetTotal": 34,
                    "ConfigAssetDecimals": 35,
                    "ConfigAssetDefaultFrozen": 36,
                    "ConfigAssetUnitName": 37,
                    "ConfigAssetName": 38,
                    "ConfigAssetURL": 39,
                    "ConfigAssetMetadataHash": 40,
                    "ConfigAssetManager": 41,
                    "ConfigAssetReserve": 42,
                    "ConfigAssetFreeze": 43,
                    "ConfigAssetClawback": 44,
                    "FreezeAsset": 45,
                    "FreezeAssetAccount": 46,
                    "FreezeAssetFrozen": 47,
                    "Assets": 48,
                    "NumAssets": 49,
                    "Applications": 50,
                    "NumApplications": 51,
                    "GlobalNumUint": 52,
                    "GlobalNumByteSlice": 53,
                    "LocalNumUint": 54,
                    "LocalNumByteSlice": 55,
                    "ExtraProgramPages": 56,
                    "Nonparticipation": 57,
                    "Logs": 58,
                    "NumLogs": 59,
                    "CreatedAssetID": 60,
                    "CreatedApplicationID": 61,
                    "LastLog": 62,
                    "StateProofPK": 63,
                    "ApprovalProgramPages": 64,
                    "NumApprovalProgramPages": 65,
                    "ClearStateProgramPages": 66,
                    "NumClearStateProgramPages": 67,
                }
            )
        ],
    ),
    "global": OpSpec(
        name="global",
        code=50,
        immediates=[
            ImmediateEnum(
                codes={
                    "MinTxnFee": 0,
                    "MinBalance": 1,
                    "MaxTxnLife": 2,
                    "ZeroAddress": 3,
                    "GroupSize": 4,
                    "LogicSigVersion": 5,
                    "Round": 6,
                    "LatestTimestamp": 7,
                    "CurrentApplicationID": 8,
                    "CreatorAddress": 9,
                    "CurrentApplicationAddress": 10,
                    "GroupID": 11,
                    "OpcodeBudget": 12,
                    "CallerApplicationID": 13,
                    "CallerApplicationAddress": 14,
                    "AssetCreateMinBalance": 15,
                    "AssetOptInMinBalance": 16,
                    "GenesisHash": 17,
                }
            )
        ],
    ),
    "gtxn": OpSpec(
        name="gtxn",
        code=51,
        immediates=[
            ImmediateKind.uint8,
            ImmediateEnum(
                codes={
                    "Sender": 0,
                    "Fee": 1,
                    "FirstValid": 2,
                    "FirstValidTime": 3,
                    "LastValid": 4,
                    "Note": 5,
                    "Lease": 6,
                    "Receiver": 7,
                    "Amount": 8,
                    "CloseRemainderTo": 9,
                    "VotePK": 10,
                    "SelectionPK": 11,
                    "VoteFirst": 12,
                    "VoteLast": 13,
                    "VoteKeyDilution": 14,
                    "Type": 15,
                    "TypeEnum": 16,
                    "XferAsset": 17,
                    "AssetAmount": 18,
                    "AssetSender": 19,
                    "AssetReceiver": 20,
                    "AssetCloseTo": 21,
                    "GroupIndex": 22,
                    "TxID": 23,
                    "ApplicationID": 24,
                    "OnCompletion": 25,
                    "ApplicationArgs": 26,
                    "NumAppArgs": 27,
                    "Accounts": 28,
                    "NumAccounts": 29,
                    "ApprovalProgram": 30,
                    "ClearStateProgram": 31,
                    "RekeyTo": 32,
                    "ConfigAsset": 33,
                    "ConfigAssetTotal": 34,
                    "ConfigAssetDecimals": 35,
                    "ConfigAssetDefaultFrozen": 36,
                    "ConfigAssetUnitName": 37,
                    "ConfigAssetName": 38,
                    "ConfigAssetURL": 39,
                    "ConfigAssetMetadataHash": 40,
                    "ConfigAssetManager": 41,
                    "ConfigAssetReserve": 42,
                    "ConfigAssetFreeze": 43,
                    "ConfigAssetClawback": 44,
                    "FreezeAsset": 45,
                    "FreezeAssetAccount": 46,
                    "FreezeAssetFrozen": 47,
                    "Assets": 48,
                    "NumAssets": 49,
                    "Applications": 50,
                    "NumApplications": 51,
                    "GlobalNumUint": 52,
                    "GlobalNumByteSlice": 53,
                    "LocalNumUint": 54,
                    "LocalNumByteSlice": 55,
                    "ExtraProgramPages": 56,
                    "Nonparticipation": 57,
                    "Logs": 58,
                    "NumLogs": 59,
                    "CreatedAssetID": 60,
                    "CreatedApplicationID": 61,
                    "LastLog": 62,
                    "StateProofPK": 63,
                    "ApprovalProgramPages": 64,
                    "NumApprovalProgramPages": 65,
                    "ClearStateProgramPages": 66,
                    "NumClearStateProgramPages": 67,
                }
            ),
        ],
    ),
    "load": OpSpec(name="load", code=52, immediates=[ImmediateKind.uint8]),
    "store": OpSpec(name="store", code=53, immediates=[ImmediateKind.uint8]),
    "txna": OpSpec(
        name="txna",
        code=54,
        immediates=[
            ImmediateEnum(
                codes={
                    "ApplicationArgs": 26,
                    "Accounts": 28,
                    "Assets": 48,
                    "Applications": 50,
                    "Logs": 58,
                    "ApprovalProgramPages": 64,
                    "ClearStateProgramPages": 66,
                }
            ),
            ImmediateKind.uint8,
        ],
    ),
    "gtxna": OpSpec(
        name="gtxna",
        code=55,
        immediates=[
            ImmediateKind.uint8,
            ImmediateEnum(
                codes={
                    "ApplicationArgs": 26,
                    "Accounts": 28,
                    "Assets": 48,
                    "Applications": 50,
                    "Logs": 58,
                    "ApprovalProgramPages": 64,
                    "ClearStateProgramPages": 66,
                }
            ),
            ImmediateKind.uint8,
        ],
    ),
    "gtxns": OpSpec(
        name="gtxns",
        code=56,
        immediates=[
            ImmediateEnum(
                codes={
                    "Sender": 0,
                    "Fee": 1,
                    "FirstValid": 2,
                    "FirstValidTime": 3,
                    "LastValid": 4,
                    "Note": 5,
                    "Lease": 6,
                    "Receiver": 7,
                    "Amount": 8,
                    "CloseRemainderTo": 9,
                    "VotePK": 10,
                    "SelectionPK": 11,
                    "VoteFirst": 12,
                    "VoteLast": 13,
                    "VoteKeyDilution": 14,
                    "Type": 15,
                    "TypeEnum": 16,
                    "XferAsset": 17,
                    "AssetAmount": 18,
                    "AssetSender": 19,
                    "AssetReceiver": 20,
                    "AssetCloseTo": 21,
                    "GroupIndex": 22,
                    "TxID": 23,
                    "ApplicationID": 24,
                    "OnCompletion": 25,
                    "ApplicationArgs": 26,
                    "NumAppArgs": 27,
                    "Accounts": 28,
                    "NumAccounts": 29,
                    "ApprovalProgram": 30,
                    "ClearStateProgram": 31,
                    "RekeyTo": 32,
                    "ConfigAsset": 33,
                    "ConfigAssetTotal": 34,
                    "ConfigAssetDecimals": 35,
                    "ConfigAssetDefaultFrozen": 36,
                    "ConfigAssetUnitName": 37,
                    "ConfigAssetName": 38,
                    "ConfigAssetURL": 39,
                    "ConfigAssetMetadataHash": 40,
                    "ConfigAssetManager": 41,
                    "ConfigAssetReserve": 42,
                    "ConfigAssetFreeze": 43,
                    "ConfigAssetClawback": 44,
                    "FreezeAsset": 45,
                    "FreezeAssetAccount": 46,
                    "FreezeAssetFrozen": 47,
                    "Assets": 48,
                    "NumAssets": 49,
                    "Applications": 50,
                    "NumApplications": 51,
                    "GlobalNumUint": 52,
                    "GlobalNumByteSlice": 53,
                    "LocalNumUint": 54,
                    "LocalNumByteSlice": 55,
                    "ExtraProgramPages": 56,
                    "Nonparticipation": 57,
                    "Logs": 58,
                    "NumLogs": 59,
                    "CreatedAssetID": 60,
                    "CreatedApplicationID": 61,
                    "LastLog": 62,
                    "StateProofPK": 63,
                    "ApprovalProgramPages": 64,
                    "NumApprovalProgramPages": 65,
                    "ClearStateProgramPages": 66,
                    "NumClearStateProgramPages": 67,
                }
            )
        ],
    ),
    "gtxnsa": OpSpec(
        name="gtxnsa",
        code=57,
        immediates=[
            ImmediateEnum(
                codes={
                    "ApplicationArgs": 26,
                    "Accounts": 28,
                    "Assets": 48,
                    "Applications": 50,
                    "Logs": 58,
                    "ApprovalProgramPages": 64,
                    "ClearStateProgramPages": 66,
                }
            ),
            ImmediateKind.uint8,
        ],
    ),
    "gload": OpSpec(name="gload", code=58, immediates=[ImmediateKind.uint8, ImmediateKind.uint8]),
    "gloads": OpSpec(name="gloads", code=59, immediates=[ImmediateKind.uint8]),
    "gaid": OpSpec(name="gaid", code=60, immediates=[ImmediateKind.uint8]),
    "gaids": OpSpec(name="gaids", code=61, immediates=[]),
    "loads": OpSpec(name="loads", code=62, immediates=[]),
    "stores": OpSpec(name="stores", code=63, immediates=[]),
    "bnz": OpSpec(name="bnz", code=64, immediates=[ImmediateKind.label]),
    "bz": OpSpec(name="bz", code=65, immediates=[ImmediateKind.label]),
    "b": OpSpec(name="b", code=66, immediates=[ImmediateKind.label]),
    "return": OpSpec(name="return", code=67, immediates=[]),
    "assert": OpSpec(name="assert", code=68, immediates=[]),
    "bury": OpSpec(name="bury", code=69, immediates=[ImmediateKind.uint8]),
    "popn": OpSpec(name="popn", code=70, immediates=[ImmediateKind.uint8]),
    "dupn": OpSpec(name="dupn", code=71, immediates=[ImmediateKind.uint8]),
    "pop": OpSpec(name="pop", code=72, immediates=[]),
    "dup": OpSpec(name="dup", code=73, immediates=[]),
    "dup2": OpSpec(name="dup2", code=74, immediates=[]),
    "dig": OpSpec(name="dig", code=75, immediates=[ImmediateKind.uint8]),
    "swap": OpSpec(name="swap", code=76, immediates=[]),
    "select": OpSpec(name="select", code=77, immediates=[]),
    "cover": OpSpec(name="cover", code=78, immediates=[ImmediateKind.uint8]),
    "uncover": OpSpec(name="uncover", code=79, immediates=[ImmediateKind.uint8]),
    "concat": OpSpec(name="concat", code=80, immediates=[]),
    "substring": OpSpec(
        name="substring", code=81, immediates=[ImmediateKind.uint8, ImmediateKind.uint8]
    ),
    "substring3": OpSpec(name="substring3", code=82, immediates=[]),
    "getbit": OpSpec(name="getbit", code=83, immediates=[]),
    "setbit": OpSpec(name="setbit", code=84, immediates=[]),
    "getbyte": OpSpec(name="getbyte", code=85, immediates=[]),
    "setbyte": OpSpec(name="setbyte", code=86, immediates=[]),
    "extract": OpSpec(
        name="extract", code=87, immediates=[ImmediateKind.uint8, ImmediateKind.uint8]
    ),
    "extract3": OpSpec(name="extract3", code=88, immediates=[]),
    "extract_uint16": OpSpec(name="extract_uint16", code=89, immediates=[]),
    "extract_uint32": OpSpec(name="extract_uint32", code=90, immediates=[]),
    "extract_uint64": OpSpec(name="extract_uint64", code=91, immediates=[]),
    "replace2": OpSpec(name="replace2", code=92, immediates=[ImmediateKind.uint8]),
    "replace3": OpSpec(name="replace3", code=93, immediates=[]),
    "base64_decode": OpSpec(
        name="base64_decode",
        code=94,
        immediates=[ImmediateEnum(codes={"URLEncoding": 0, "StdEncoding": 1})],
    ),
    "json_ref": OpSpec(
        name="json_ref",
        code=95,
        immediates=[ImmediateEnum(codes={"JSONString": 0, "JSONUint64": 1, "JSONObject": 2})],
    ),
    "balance": OpSpec(name="balance", code=96, immediates=[]),
    "app_opted_in": OpSpec(name="app_opted_in", code=97, immediates=[]),
    "app_local_get": OpSpec(name="app_local_get", code=98, immediates=[]),
    "app_local_get_ex": OpSpec(name="app_local_get_ex", code=99, immediates=[]),
    "app_global_get": OpSpec(name="app_global_get", code=100, immediates=[]),
    "app_global_get_ex": OpSpec(name="app_global_get_ex", code=101, immediates=[]),
    "app_local_put": OpSpec(name="app_local_put", code=102, immediates=[]),
    "app_global_put": OpSpec(name="app_global_put", code=103, immediates=[]),
    "app_local_del": OpSpec(name="app_local_del", code=104, immediates=[]),
    "app_global_del": OpSpec(name="app_global_del", code=105, immediates=[]),
    "asset_holding_get": OpSpec(
        name="asset_holding_get",
        code=112,
        immediates=[ImmediateEnum(codes={"AssetBalance": 0, "AssetFrozen": 1})],
    ),
    "asset_params_get": OpSpec(
        name="asset_params_get",
        code=113,
        immediates=[
            ImmediateEnum(
                codes={
                    "AssetTotal": 0,
                    "AssetDecimals": 1,
                    "AssetDefaultFrozen": 2,
                    "AssetUnitName": 3,
                    "AssetName": 4,
                    "AssetURL": 5,
                    "AssetMetadataHash": 6,
                    "AssetManager": 7,
                    "AssetReserve": 8,
                    "AssetFreeze": 9,
                    "AssetClawback": 10,
                    "AssetCreator": 11,
                }
            )
        ],
    ),
    "app_params_get": OpSpec(
        name="app_params_get",
        code=114,
        immediates=[
            ImmediateEnum(
                codes={
                    "AppApprovalProgram": 0,
                    "AppClearStateProgram": 1,
                    "AppGlobalNumUint": 2,
                    "AppGlobalNumByteSlice": 3,
                    "AppLocalNumUint": 4,
                    "AppLocalNumByteSlice": 5,
                    "AppExtraProgramPages": 6,
                    "AppCreator": 7,
                    "AppAddress": 8,
                }
            )
        ],
    ),
    "acct_params_get": OpSpec(
        name="acct_params_get",
        code=115,
        immediates=[
            ImmediateEnum(
                codes={
                    "AcctBalance": 0,
                    "AcctMinBalance": 1,
                    "AcctAuthAddr": 2,
                    "AcctTotalNumUint": 3,
                    "AcctTotalNumByteSlice": 4,
                    "AcctTotalExtraAppPages": 5,
                    "AcctTotalAppsCreated": 6,
                    "AcctTotalAppsOptedIn": 7,
                    "AcctTotalAssetsCreated": 8,
                    "AcctTotalAssets": 9,
                    "AcctTotalBoxes": 10,
                    "AcctTotalBoxBytes": 11,
                }
            )
        ],
    ),
    "min_balance": OpSpec(name="min_balance", code=120, immediates=[]),
    "pushbytes": OpSpec(name="pushbytes", code=128, immediates=[ImmediateKind.bytes]),
    "pushint": OpSpec(name="pushint", code=129, immediates=[ImmediateKind.varuint]),
    "pushbytess": OpSpec(name="pushbytess", code=130, immediates=[ImmediateKind.bytes_array]),
    "pushints": OpSpec(name="pushints", code=131, immediates=[ImmediateKind.varuint_array]),
    "ed25519verify_bare": OpSpec(name="ed25519verify_bare", code=132, immediates=[]),
    "callsub": OpSpec(name="callsub", code=136, immediates=[ImmediateKind.label]),
    "retsub": OpSpec(name="retsub", code=137, immediates=[]),
    "proto": OpSpec(name="proto", code=138, immediates=[ImmediateKind.uint8, ImmediateKind.uint8]),
    "frame_dig": OpSpec(name="frame_dig", code=139, immediates=[ImmediateKind.int8]),
    "frame_bury": OpSpec(name="frame_bury", code=140, immediates=[ImmediateKind.int8]),
    "switch": OpSpec(name="switch", code=141, immediates=[ImmediateKind.label_array]),
    "match": OpSpec(name="match", code=142, immediates=[ImmediateKind.label_array]),
    "shl": OpSpec(name="shl", code=144, immediates=[]),
    "shr": OpSpec(name="shr", code=145, immediates=[]),
    "sqrt": OpSpec(name="sqrt", code=146, immediates=[]),
    "bitlen": OpSpec(name="bitlen", code=147, immediates=[]),
    "exp": OpSpec(name="exp", code=148, immediates=[]),
    "expw": OpSpec(name="expw", code=149, immediates=[]),
    "bsqrt": OpSpec(name="bsqrt", code=150, immediates=[]),
    "divw": OpSpec(name="divw", code=151, immediates=[]),
    "sha3_256": OpSpec(name="sha3_256", code=152, immediates=[]),
    "b+": OpSpec(name="b+", code=160, immediates=[]),
    "b-": OpSpec(name="b-", code=161, immediates=[]),
    "b/": OpSpec(name="b/", code=162, immediates=[]),
    "b*": OpSpec(name="b*", code=163, immediates=[]),
    "b<": OpSpec(name="b<", code=164, immediates=[]),
    "b>": OpSpec(name="b>", code=165, immediates=[]),
    "b<=": OpSpec(name="b<=", code=166, immediates=[]),
    "b>=": OpSpec(name="b>=", code=167, immediates=[]),
    "b==": OpSpec(name="b==", code=168, immediates=[]),
    "b!=": OpSpec(name="b!=", code=169, immediates=[]),
    "b%": OpSpec(name="b%", code=170, immediates=[]),
    "b|": OpSpec(name="b|", code=171, immediates=[]),
    "b&": OpSpec(name="b&", code=172, immediates=[]),
    "b^": OpSpec(name="b^", code=173, immediates=[]),
    "b~": OpSpec(name="b~", code=174, immediates=[]),
    "bzero": OpSpec(name="bzero", code=175, immediates=[]),
    "log": OpSpec(name="log", code=176, immediates=[]),
    "itxn_begin": OpSpec(name="itxn_begin", code=177, immediates=[]),
    "itxn_field": OpSpec(
        name="itxn_field",
        code=178,
        immediates=[
            ImmediateEnum(
                codes={
                    "Sender": 0,
                    "Fee": 1,
                    "Note": 5,
                    "Receiver": 7,
                    "Amount": 8,
                    "CloseRemainderTo": 9,
                    "VotePK": 10,
                    "SelectionPK": 11,
                    "VoteFirst": 12,
                    "VoteLast": 13,
                    "VoteKeyDilution": 14,
                    "Type": 15,
                    "TypeEnum": 16,
                    "XferAsset": 17,
                    "AssetAmount": 18,
                    "AssetSender": 19,
                    "AssetReceiver": 20,
                    "AssetCloseTo": 21,
                    "ApplicationID": 24,
                    "OnCompletion": 25,
                    "ApplicationArgs": 26,
                    "Accounts": 28,
                    "ApprovalProgram": 30,
                    "ClearStateProgram": 31,
                    "RekeyTo": 32,
                    "ConfigAsset": 33,
                    "ConfigAssetTotal": 34,
                    "ConfigAssetDecimals": 35,
                    "ConfigAssetDefaultFrozen": 36,
                    "ConfigAssetUnitName": 37,
                    "ConfigAssetName": 38,
                    "ConfigAssetURL": 39,
                    "ConfigAssetMetadataHash": 40,
                    "ConfigAssetManager": 41,
                    "ConfigAssetReserve": 42,
                    "ConfigAssetFreeze": 43,
                    "ConfigAssetClawback": 44,
                    "FreezeAsset": 45,
                    "FreezeAssetAccount": 46,
                    "FreezeAssetFrozen": 47,
                    "Assets": 48,
                    "Applications": 50,
                    "GlobalNumUint": 52,
                    "GlobalNumByteSlice": 53,
                    "LocalNumUint": 54,
                    "LocalNumByteSlice": 55,
                    "ExtraProgramPages": 56,
                    "Nonparticipation": 57,
                    "StateProofPK": 63,
                    "ApprovalProgramPages": 64,
                    "ClearStateProgramPages": 66,
                }
            )
        ],
    ),
    "itxn_submit": OpSpec(name="itxn_submit", code=179, immediates=[]),
    "itxn": OpSpec(
        name="itxn",
        code=180,
        immediates=[
            ImmediateEnum(
                codes={
                    "Sender": 0,
                    "Fee": 1,
                    "FirstValid": 2,
                    "FirstValidTime": 3,
                    "LastValid": 4,
                    "Note": 5,
                    "Lease": 6,
                    "Receiver": 7,
                    "Amount": 8,
                    "CloseRemainderTo": 9,
                    "VotePK": 10,
                    "SelectionPK": 11,
                    "VoteFirst": 12,
                    "VoteLast": 13,
                    "VoteKeyDilution": 14,
                    "Type": 15,
                    "TypeEnum": 16,
                    "XferAsset": 17,
                    "AssetAmount": 18,
                    "AssetSender": 19,
                    "AssetReceiver": 20,
                    "AssetCloseTo": 21,
                    "GroupIndex": 22,
                    "TxID": 23,
                    "ApplicationID": 24,
                    "OnCompletion": 25,
                    "ApplicationArgs": 26,
                    "NumAppArgs": 27,
                    "Accounts": 28,
                    "NumAccounts": 29,
                    "ApprovalProgram": 30,
                    "ClearStateProgram": 31,
                    "RekeyTo": 32,
                    "ConfigAsset": 33,
                    "ConfigAssetTotal": 34,
                    "ConfigAssetDecimals": 35,
                    "ConfigAssetDefaultFrozen": 36,
                    "ConfigAssetUnitName": 37,
                    "ConfigAssetName": 38,
                    "ConfigAssetURL": 39,
                    "ConfigAssetMetadataHash": 40,
                    "ConfigAssetManager": 41,
                    "ConfigAssetReserve": 42,
                    "ConfigAssetFreeze": 43,
                    "ConfigAssetClawback": 44,
                    "FreezeAsset": 45,
                    "FreezeAssetAccount": 46,
                    "FreezeAssetFrozen": 47,
                    "Assets": 48,
                    "NumAssets": 49,
                    "Applications": 50,
                    "NumApplications": 51,
                    "GlobalNumUint": 52,
                    "GlobalNumByteSlice": 53,
                    "LocalNumUint": 54,
                    "LocalNumByteSlice": 55,
                    "ExtraProgramPages": 56,
                    "Nonparticipation": 57,
                    "Logs": 58,
                    "NumLogs": 59,
                    "CreatedAssetID": 60,
                    "CreatedApplicationID": 61,
                    "LastLog": 62,
                    "StateProofPK": 63,
                    "ApprovalProgramPages": 64,
                    "NumApprovalProgramPages": 65,
                    "ClearStateProgramPages": 66,
                    "NumClearStateProgramPages": 67,
                }
            )
        ],
    ),
    "itxna": OpSpec(
        name="itxna",
        code=181,
        immediates=[
            ImmediateEnum(
                codes={
                    "ApplicationArgs": 26,
                    "Accounts": 28,
                    "Assets": 48,
                    "Applications": 50,
                    "Logs": 58,
                    "ApprovalProgramPages": 64,
                    "ClearStateProgramPages": 66,
                }
            ),
            ImmediateKind.uint8,
        ],
    ),
    "itxn_next": OpSpec(name="itxn_next", code=182, immediates=[]),
    "gitxn": OpSpec(
        name="gitxn",
        code=183,
        immediates=[
            ImmediateKind.uint8,
            ImmediateEnum(
                codes={
                    "Sender": 0,
                    "Fee": 1,
                    "FirstValid": 2,
                    "FirstValidTime": 3,
                    "LastValid": 4,
                    "Note": 5,
                    "Lease": 6,
                    "Receiver": 7,
                    "Amount": 8,
                    "CloseRemainderTo": 9,
                    "VotePK": 10,
                    "SelectionPK": 11,
                    "VoteFirst": 12,
                    "VoteLast": 13,
                    "VoteKeyDilution": 14,
                    "Type": 15,
                    "TypeEnum": 16,
                    "XferAsset": 17,
                    "AssetAmount": 18,
                    "AssetSender": 19,
                    "AssetReceiver": 20,
                    "AssetCloseTo": 21,
                    "GroupIndex": 22,
                    "TxID": 23,
                    "ApplicationID": 24,
                    "OnCompletion": 25,
                    "ApplicationArgs": 26,
                    "NumAppArgs": 27,
                    "Accounts": 28,
                    "NumAccounts": 29,
                    "ApprovalProgram": 30,
                    "ClearStateProgram": 31,
                    "RekeyTo": 32,
                    "ConfigAsset": 33,
                    "ConfigAssetTotal": 34,
                    "ConfigAssetDecimals": 35,
                    "ConfigAssetDefaultFrozen": 36,
                    "ConfigAssetUnitName": 37,
                    "ConfigAssetName": 38,
                    "ConfigAssetURL": 39,
                    "ConfigAssetMetadataHash": 40,
                    "ConfigAssetManager": 41,
                    "ConfigAssetReserve": 42,
                    "ConfigAssetFreeze": 43,
                    "ConfigAssetClawback": 44,
                    "FreezeAsset": 45,
                    "FreezeAssetAccount": 46,
                    "FreezeAssetFrozen": 47,
                    "Assets": 48,
                    "NumAssets": 49,
                    "Applications": 50,
                    "NumApplications": 51,
                    "GlobalNumUint": 52,
                    "GlobalNumByteSlice": 53,
                    "LocalNumUint": 54,
                    "LocalNumByteSlice": 55,
                    "ExtraProgramPages": 56,
                    "Nonparticipation": 57,
                    "Logs": 58,
                    "NumLogs": 59,
                    "CreatedAssetID": 60,
                    "CreatedApplicationID": 61,
                    "LastLog": 62,
                    "StateProofPK": 63,
                    "ApprovalProgramPages": 64,
                    "NumApprovalProgramPages": 65,
                    "ClearStateProgramPages": 66,
                    "NumClearStateProgramPages": 67,
                }
            ),
        ],
    ),
    "gitxna": OpSpec(
        name="gitxna",
        code=184,
        immediates=[
            ImmediateKind.uint8,
            ImmediateEnum(
                codes={
                    "ApplicationArgs": 26,
                    "Accounts": 28,
                    "Assets": 48,
                    "Applications": 50,
                    "Logs": 58,
                    "ApprovalProgramPages": 64,
                    "ClearStateProgramPages": 66,
                }
            ),
            ImmediateKind.uint8,
        ],
    ),
    "box_create": OpSpec(name="box_create", code=185, immediates=[]),
    "box_extract": OpSpec(name="box_extract", code=186, immediates=[]),
    "box_replace": OpSpec(name="box_replace", code=187, immediates=[]),
    "box_del": OpSpec(name="box_del", code=188, immediates=[]),
    "box_len": OpSpec(name="box_len", code=189, immediates=[]),
    "box_get": OpSpec(name="box_get", code=190, immediates=[]),
    "box_put": OpSpec(name="box_put", code=191, immediates=[]),
    "txnas": OpSpec(
        name="txnas",
        code=192,
        immediates=[
            ImmediateEnum(
                codes={
                    "ApplicationArgs": 26,
                    "Accounts": 28,
                    "Assets": 48,
                    "Applications": 50,
                    "Logs": 58,
                    "ApprovalProgramPages": 64,
                    "ClearStateProgramPages": 66,
                }
            )
        ],
    ),
    "gtxnas": OpSpec(
        name="gtxnas",
        code=193,
        immediates=[
            ImmediateKind.uint8,
            ImmediateEnum(
                codes={
                    "ApplicationArgs": 26,
                    "Accounts": 28,
                    "Assets": 48,
                    "Applications": 50,
                    "Logs": 58,
                    "ApprovalProgramPages": 64,
                    "ClearStateProgramPages": 66,
                }
            ),
        ],
    ),
    "gtxnsas": OpSpec(
        name="gtxnsas",
        code=194,
        immediates=[
            ImmediateEnum(
                codes={
                    "ApplicationArgs": 26,
                    "Accounts": 28,
                    "Assets": 48,
                    "Applications": 50,
                    "Logs": 58,
                    "ApprovalProgramPages": 64,
                    "ClearStateProgramPages": 66,
                }
            )
        ],
    ),
    "args": OpSpec(name="args", code=195, immediates=[]),
    "gloadss": OpSpec(name="gloadss", code=196, immediates=[]),
    "itxnas": OpSpec(
        name="itxnas",
        code=197,
        immediates=[
            ImmediateEnum(
                codes={
                    "ApplicationArgs": 26,
                    "Accounts": 28,
                    "Assets": 48,
                    "Applications": 50,
                    "Logs": 58,
                    "ApprovalProgramPages": 64,
                    "ClearStateProgramPages": 66,
                }
            )
        ],
    ),
    "gitxnas": OpSpec(
        name="gitxnas",
        code=198,
        immediates=[
            ImmediateKind.uint8,
            ImmediateEnum(
                codes={
                    "ApplicationArgs": 26,
                    "Accounts": 28,
                    "Assets": 48,
                    "Applications": 50,
                    "Logs": 58,
                    "ApprovalProgramPages": 64,
                    "ClearStateProgramPages": 66,
                }
            ),
        ],
    ),
    "vrf_verify": OpSpec(
        name="vrf_verify", code=208, immediates=[ImmediateEnum(codes={"VrfAlgorand": 0})]
    ),
    "block": OpSpec(
        name="block", code=209, immediates=[ImmediateEnum(codes={"BlkSeed": 0, "BlkTimestamp": 1})]
    ),
    "box_splice": OpSpec(name="box_splice", code=210, immediates=[]),
    "box_resize": OpSpec(name="box_resize", code=211, immediates=[]),
    "ec_add": OpSpec(
        name="ec_add",
        code=224,
        immediates=[
            ImmediateEnum(codes={"BN254g1": 0, "BN254g2": 1, "BLS12_381g1": 2, "BLS12_381g2": 3})
        ],
    ),
    "ec_scalar_mul": OpSpec(
        name="ec_scalar_mul",
        code=225,
        immediates=[
            ImmediateEnum(codes={"BN254g1": 0, "BN254g2": 1, "BLS12_381g1": 2, "BLS12_381g2": 3})
        ],
    ),
    "ec_pairing_check": OpSpec(
        name="ec_pairing_check",
        code=226,
        immediates=[
            ImmediateEnum(codes={"BN254g1": 0, "BN254g2": 1, "BLS12_381g1": 2, "BLS12_381g2": 3})
        ],
    ),
    "ec_multi_scalar_mul": OpSpec(
        name="ec_multi_scalar_mul",
        code=227,
        immediates=[
            ImmediateEnum(codes={"BN254g1": 0, "BN254g2": 1, "BLS12_381g1": 2, "BLS12_381g2": 3})
        ],
    ),
    "ec_subgroup_check": OpSpec(
        name="ec_subgroup_check",
        code=228,
        immediates=[
            ImmediateEnum(codes={"BN254g1": 0, "BN254g2": 1, "BLS12_381g1": 2, "BLS12_381g2": 3})
        ],
    ),
    "ec_map_to": OpSpec(
        name="ec_map_to",
        code=229,
        immediates=[
            ImmediateEnum(codes={"BN254g1": 0, "BN254g2": 1, "BLS12_381g1": 2, "BLS12_381g2": 3})
        ],
    ),
}