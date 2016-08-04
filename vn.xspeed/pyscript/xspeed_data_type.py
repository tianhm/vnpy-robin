# encoding: UTF-8

defineDict = {}
typedefDict = {}


#/////////////////////////////////////////////////////////
#DFITCUserIDType：用户ID数据类型
#/////////////////////////////////////////////////////////
typedefDict["DFITCUserIDType"] = "string"


#/////////////////////////////////////////////////////////
#DFITCAccountIDType：资金账户数据类型
#/////////////////////////////////////////////////////////
typedefDict["DFITCAccountIDType"] = "string"


#/////////////////////////////////////////////////////////
#DFITCExecStateType：执行状态数据类型
#/////////////////////////////////////////////////////////
typedefDict["DFITCExecStateType"] = "int"
#成功
defineDict["DFITC_SUCCESS"] = 0
#失败
defineDict["DFITC_FAIL"] = 1


#/////////////////////////////////////////////////////////
#DFITCClientIDType：交易编码数据类型
#/////////////////////////////////////////////////////////
typedefDict["DFITCClientIDType"] = "string"


#/////////////////////////////////////////////////////////
#DFITCClientStatusType：交易编码状态数据类型
#/////////////////////////////////////////////////////////
typedefDict["DFITCClientStatusType"] = "int"
#禁止开新仓
defineDict["DFITC_PROHIBIT_OPEN"] = 4
#允许开新仓
defineDict["DFITC_ALLOW_OPEN"] = 5


#/////////////////////////////////////////////////////////
#DFITCInstrumentIDType：合约代码数据类型
#/////////////////////////////////////////////////////////
typedefDict["DFITCInstrumentIDType"] = "string"

#/////////////////////////////////////////////////////////
#DFITCInstrumentPrefixType：品种名称数据类型
#/////////////////////////////////////////////////////////
typedefDict["DFITCInstrumentPrefixType"] = "string"

#/////////////////////////////////////////////////////////
#DFITCVarietyNameType：品种名称数据类型
#/////////////////////////////////////////////////////////
typedefDict["DFITCVarietyNameType"] = "string"


#/////////////////////////////////////////////////////////
#DFITCInstrumentNameType：合约名称数据类型
#/////////////////////////////////////////////////////////
typedefDict["DFITCInstrumentNameType"] = "string"


#/////////////////////////////////////////////////////////
#DFITCActiveContractType：有效合约数据类型
#/////////////////////////////////////////////////////////
typedefDict["DFITCActiveContractType"] = "string"


#/////////////////////////////////////////////////////////
#DFITCLocalOrderIDType:本地委托号数据类型
#/////////////////////////////////////////////////////////
typedefDict["DFITCLocalOrderIDType"] = "long"


#/////////////////////////////////////////////////////////
#DFITCPriceType:价格数据类型
#/////////////////////////////////////////////////////////
typedefDict["DFITCPriceType"] = "float"


#/////////////////////////////////////////////////////////
#DFITCAmountType:委托数量数据类型
#/////////////////////////////////////////////////////////
typedefDict["DFITCAmountType"] = "long"


#/////////////////////////////////////////////////////////
#DFITCBuySellTypeType:买卖数据类型
#/////////////////////////////////////////////////////////
typedefDict["DFITCBuySellTypeType"] = "short"
#买
defineDict["DFITC_SPD_BUY"] = 1
#卖
defineDict["DFITC_SPD_SELL"] = 2


#/////////////////////////////////////////////////////////
#DFITCOpenCloseTypeType：开平标志数据类型
#/////////////////////////////////////////////////////////
typedefDict["DFITCOpenCloseTypeType"] = "int"
#开仓
defineDict["DFITC_SPD_OPEN"] = 1
#平仓
defineDict["DFITC_SPD_CLOSE"] = 2
#平今
defineDict["DFITC_SPD_CLOSETODAY"] = 4
#期权执行
defineDict["DFITC_SPD_EXECUTE"] = 6
#期权放弃
defineDict["DFITC_SPD_GIVEUP"] = 7
#期权履约
defineDict["DFITC_SPD_PERFORM"] = 8
#询价
defineDict["DFITC_SPD_OPTQRYPRICE"] = 9
#强平
defineDict["DFITC_SPD_FORCECLOSE"] = 12
#强平今
defineDict["DFITC_SPD_FORCECLOSETODAY"] = 14


#/////////////////////////////////////////////////////////
#DFITCSpeculationValueType:投机保值数据类型
#/////////////////////////////////////////////////////////
typedefDict["DFITCSpeculationValueType"] = "short"


#/////////////////////////////////////////////////////////
#DFITCExchangeIDType:交易所编码数据类型
#/////////////////////////////////////////////////////////
typedefDict["DFITCExchangeIDType"] = "string"
#大商所
defineDict["DFITC_EXCHANGE_DCE"] = "DCE"
#郑商所
defineDict["DFITC_EXCHANGE_CZCE"] = "CZCE"
#上期所
defineDict["DFITC_EXCHANGE_SHFE"] = "SHFE"
#中金所
defineDict["DFITC_EXCHANGE_CFFEX"] = "CFFEX"
#上能所
defineDict["DFITC_EXCHANGE_INE"] = "INE"


#/////////////////////////////////////////////////////////
#DFITCFrontAddrType:前置机地址数据类型
#/////////////////////////////////////////////////////////
typedefDict["DFITCFrontAddrType"] = "string"


#/////////////////////////////////////////////////////////
#DFITCCompanyIDType:开发商代码数据类型
#/////////////////////////////////////////////////////////
typedefDict["DFITCCompanyIDType"] = "short"


#/////////////////////////////////////////////////////////
#DFITCPasswdType:用户密码数据类型
#柜台端密码不能为空且有效长度最大为16位
#/////////////////////////////////////////////////////////
typedefDict["DFITCPasswdType"] = "string"


#/////////////////////////////////////////////////////////
#DFITCSPDOrderIDType:柜台委托号数据类型
#柜台委托号和条件单号使用相同字段表示
#当DFITCSPDOrderIDType的取值为正数[最小为1 ]，表示为柜台委
#托号，该笔报单已经到柜台
#当DFITCSPDOrderIDType的取值为负数[最大为-2]，标示为条件单
#号，该笔报单在条件单模块
#/////////////////////////////////////////////////////////
typedefDict["DFITCSPDOrderIDType"] = "long"


#/////////////////////////////////////////////////////////
#DFITCOrderSysIDType:报单编号数据类型
#/////////////////////////////////////////////////////////
typedefDict["DFITCOrderSysIDType"] = "string"


#/////////////////////////////////////////////////////////
#DFITCOrderType:报单类型
#/////////////////////////////////////////////////////////
typedefDict["DFITCOrderTypeType"] = "int"
#限价委托
defineDict["DFITC_LIMITORDER"] = 1
#市价委托
defineDict["DFITC_MKORDER"] = 2
#套利委托
defineDict["DFITC_ARBITRAGE"] = 4
#展期互换委托
defineDict["DFITC_EXTENSION"] = 8
#限价止盈委托
defineDict["DFITC_PROFIT_LIMITORDER"] = 32
#市价止盈委托
defineDict["DFITC_PROFIT_MKORDER"] = 34
#限价止损委托
defineDict["DFITC_LOSS_LIMITORDER"] = 48
#市价止损委托
defineDict["DFITC_LOSS_MKORDER"] = 50

#/////////////////////////////////////////////////////////
#DFITCOrderAnswerStatusType:委托回报类型
#/////////////////////////////////////////////////////////
typedefDict["DFITCOrderAnswerStatusType"] = "short"
#全部撤单
defineDict["DFITC_SPD_CANCELED"] = 1
#全部成交
defineDict["DFITC_SPD_FILLED"] = 2
#未成交还在队列中
defineDict["DFITC_SPD_IN_QUEUE"] = 3
#部分成交还在队列中
defineDict["DFITC_SPD_PARTIAL"] = 4
#部成部撤
defineDict["DFITC_SPD_PARTIAL_CANCELED"] = 5
#撤单中
defineDict["DFITC_SPD_IN_CANCELING"] = 6
#错误(废单错误)
defineDict["DFITC_SPD_ERROR"] = 7
#未成交不在队列中
defineDict["DFITC_SPD_PLACED"] = 8
#柜台已接收，但尚未到交易所
defineDict["DFITC_SPD_TRIGGERED"] = 10


#////////////////////////////////////////////////////////////
#基于算法单模块新增
#////////////////////////////////////////////////////////////

#未触发
defineDict["DFITC_EXT_UNTRIGGER"] = 13
#部分触发
defineDict["DFITC_EXT_PART_TRIGGER"] = 14
#全部触发
defineDict["DFITC_EXT_ALL_TRIGGER"] = 15
#已经撤单
defineDict["DFITC_EXT_CANCELLED"] = 16
#报单失败
defineDict[""] = 17


#/////////////////////////////////////////////////////////
#DFITCMatchIDType:成交编号数据类型
#/////////////////////////////////////////////////////////
typedefDict["DFITCMatchIDType"] = "string"


#/////////////////////////////////////////////////////////
#DFITCDateType：时间数据类型
#/////////////////////////////////////////////////////////
typedefDict["DFITCDateType"] = "string"


#/////////////////////////////////////////////////////////
#DFITCMatchType:成交类型数据类型
#/////////////////////////////////////////////////////////
typedefDict["DFITCMatchType"] = "long"
#普通成交
defineDict["DFITC_BASIC_TRADE"] = 0


#/////////////////////////////////////////////////////////
#DFITCSpeculatorType:投保类型
#/////////////////////////////////////////////////////////
typedefDict["DFITCSpeculatorType"] = "int"
#投机
defineDict["DFITC_SPD_SPECULATOR"] = 0
#套保
defineDict["DFITC_SPD_HEDGE"] = 1
#套利
defineDict["DFITC_SPD_ARBITRAGE"] = 2


#/////////////////////////////////////////////////////////
#DFITCFeeType:手续费数据类型
#/////////////////////////////////////////////////////////
typedefDict["DFITCFeeType"] = "float"


#/////////////////////////////////////////////////////////
#DFITCErrorIDType:错误数据类型
#/////////////////////////////////////////////////////////
typedefDict["DFITCErrorIDType"] = "int"


#/////////////////////////////////////////////////////////
#DFITCErrorMsgInfoType:错误信息数据类型
#/////////////////////////////////////////////////////////
typedefDict["DFITCErrorMsgInfoType"] = "string"


#/////////////////////////////////////////////////////////
#DFITCMsgInfoType:消息信息数据类型
#/////////////////////////////////////////////////////////
typedefDict["DFITCMsgInfoType"] = "string"


#/////////////////////////////////////////////////////////
#DFITCEquityType:权益数据类型
#/////////////////////////////////////////////////////////
typedefDict["DFITCEquityType"] = "float"


#/////////////////////////////////////////////////////////
#DFITCProfitLossType:盈亏数据类型
#/////////////////////////////////////////////////////////
typedefDict["DFITCProfitLossType"] = "float"


#/////////////////////////////////////////////////////////
#DFITCAccountLoginResultType:资金账户登录结果
#/////////////////////////////////////////////////////////
typedefDict["DFITCAccountLoginResultType"] = "int"
#登录成功
defineDict["DFITC_LOGIN_SUCCESS"] = 0
#登录失败
defineDict["DFITC_LOGIN_FAILED"] = 1
#已退出
defineDict["DFITC_LOGIN_QUIT"] = 2
#未操作
defineDict["DFITC_LOGIN_NOT_OPERATE"] = 9


#/////////////////////////////////////////////////////////
#DFITCSessionIDType:SessionID数据类型
#/////////////////////////////////////////////////////////
typedefDict["DFITCSessionIDType"] = "long"


#/////////////////////////////////////////////////////////
#DFITCAccountLogoutResultType:资金帐号登出结果
#/////////////////////////////////////////////////////////
typedefDict["DFITCAccountLogoutResultType"] = "int"
#登出成功
defineDict["DFITC_LOGOUT_SUCCESS"] = 0
#登出失败
defineDict["DFITC_LOGOUT_FAILED"] = 1


#/////////////////////////////////////////////////////////
#DFITCUserTypeType:用户类型
#/////////////////////////////////////////////////////////
typedefDict["DFITCUserTypeType"] = "int"


#/////////////////////////////////////////////////////////
#DFITCCounterIDType:柜台编号数据类型
#/////////////////////////////////////////////////////////
typedefDict["DFITCCounterIDType"] = "int"


#/////////////////////////////////////////////////////////
#DFITCRiskDegreeType:风险度数据类型
#/////////////////////////////////////////////////////////
typedefDict["DFITCRiskDegreeType"] = "float"


#/////////////////////////////////////////////////////////
#DFITCMilliSecType:微秒数据类型
#/////////////////////////////////////////////////////////
typedefDict["DFITCMilliSecType"] = "int"


#/////////////////////////////////////////////////////////
#DFITCDeltaType:虚实度数据类型
#/////////////////////////////////////////////////////////
typedefDict["DFITCDeltaType"] = "float"


#/////////////////////////////////////////////////////////
#DFITCVolumeType：数量数据类型
#/////////////////////////////////////////////////////////
typedefDict["DFITCVolumeType"] = "int"


#/////////////////////////////////////////////////////////
#DFITCFrontIDType:前置机编号数据类型
#/////////////////////////////////////////////////////////
typedefDict["DFITCFrontIDType"] = "int"


#/////////////////////////////////////////////////////////
#DFITCOfferPriceLimitType:报价数据上限数据类型
#/////////////////////////////////////////////////////////
typedefDict["DFITCOfferPriceLimitType"] = "int"


#/////////////////////////////////////////////////////////
#DFITCOrderNumType:委托号数据类型
#/////////////////////////////////////////////////////////
typedefDict["DFITCOrderNumType"] = "short"


#/////////////////////////////////////////////////////////
#DFITCRatioType:比率数据类型
#/////////////////////////////////////////////////////////
typedefDict["DFITCRatioType"] = "float"


#/////////////////////////////////////////////////////////
#DFITCPremiumType:权利金
#/////////////////////////////////////////////////////////
typedefDict["DFITCPremiumType"] = "float"


#/////////////////////////////////////////////////////////
#DFITCMarketValueType:期权市值
#/////////////////////////////////////////////////////////
typedefDict["DFITCMarketValueType"] = "float"


#/////////////////////////////////////////////////////////
#DFITCTimeType:交易所时间
#/////////////////////////////////////////////////////////
typedefDict["DFITCTimeType"] = "string"


#/////////////////////////////////////////////////////////
#DFITCAbiPolicyCodeType: 套利策略代码数据类型
#/////////////////////////////////////////////////////////
typedefDict["DFITCAbiPolicyCodeType"] = "string"
#跨期套利
defineDict["DFITC_SP"] = "SP"
#两腿跨品种套利
defineDict["DFITC_SP_SPC"] = "SPC"
#压榨套利
defineDict["DFITC_SP_SPX"] = "SPX"
#Call Spread
defineDict["DFITC_SP_CALL"] = "CSPR"
#Put Spread
defineDict["DFITC_SP_PUT"] = "PSPR"
#Combo
defineDict["DFITC_SP_COMBO"] = "COMBO"
#Straddle
defineDict["DFITC_SP_STRADDLE"] = "STD"
#Strangle
defineDict["DFITC_SP_STRANGLE"] = "STG"
#Guts
defineDict["DFITC_SP_GUTS"] = "GUTS"
#Synthetic Underlying
defineDict["DFITC_SP_SYNUND"] = "SYN"


#/////////////////////////////////////////////////////////
#DFITCOrderPropertyType:订单属性
#/////////////////////////////////////////////////////////
typedefDict["DFITCOrderPropertyType"] = "char"
#无订单属性
defineDict["DFITC_SP_NON"] = '0'
#FAK设置
defineDict["DFITC_SP_FAK"] = '1'
#FOK设置
defineDict["DFITC_SP_FOK"] = '2'
#市价任意价
defineDict["DFITC_SP_ANYPRICE"] = '3'
#市价任意价转限价
defineDict["DFITC_SP_ANYPRICE_TO_MKORDER"] = '4'
#五档市价
defineDict["DFITC_SP_FIVELEVELPRICE"] = '5'
#五档市价转限价
defineDict["DFITC_SP_FIVELEVELPRICE_TO_LIMIT"] = '6'
#最优价
defineDict["DFITC_SP_BESTPRICE"] = '7'
#最优价转限价
defineDict["DFITC_SP_BESTPRICE_TO_LIMIT"] = '8'



#/////////////////////////////////////////////////////////
#DFITCInsertType:委托类别
#/////////////////////////////////////////////////////////
typedefDict["DFITCInsertType"] = "int"
#普通委托单
defineDict["DFITC_BASIC_ORDER"] = 0x0001
#自动单
defineDict["DFITC_AUTO_ORDER"] = 0x0002


#/////////////////////////////////////////////////////////
#DFITCOptionTypeType:期权类别数据类型
#/////////////////////////////////////////////////////////
typedefDict["DFITCOptionTypeType"] = "int"
#看涨
defineDict["DFITC_OPT_CALL"] = 1
#看跌
defineDict["DFITC_OPT_PUT"] = 2


#/////////////////////////////////////////////////////////
#DFITCInstrumentTypeType:合约类型数据类型
#/////////////////////////////////////////////////////////
typedefDict["DFITCInstrumentTypeType"] = "int"
#期货
defineDict["DFITC_COMM_TYPE"] = 0
#期权
defineDict["DFITC_OPT_TYPE"] = 1


#/////////////////////////////////////////////////////////
#DFITCCancelTypeType:撤销标志数据类型
#/////////////////////////////////////////////////////////
typedefDict["DFITCCancelTypeType"] = "char"
#订单
defineDict["DFITC_ORDER_BOOK"] = 'O'
#撤销
defineDict["DFITC_ORDER_CANCEL"] = 'W'


#/////////////////////////////////////////////////////////
#DFITCContentType:消息正文数据类型
#/////////////////////////////////////////////////////////
typedefDict["DFITCContentType"] = "string"


#/////////////////////////////////////////////////////////
#DFITCInstrumentStatusType:合约交易状态数据类型
#/////////////////////////////////////////////////////////
typedefDict["DFITCInstrumentStatusType"] = "int"


#/////////////////////////////////////////////////////////
#DFITCInstStatusEnterReasonType:进入本状态原因数据类型
#/////////////////////////////////////////////////////////
typedefDict["DFITCInstStatusEnterReasonType"] = "short"


#/////////////////////////////////////////////////////////
#DFITCCurrencyType:币种数据类型
#/////////////////////////////////////////////////////////
typedefDict["DFITCCurrencyType"] = "string"


#/////////////////////////////////////////////////////////
#DFITCConfirmType:确认标志数据类型
#/////////////////////////////////////////////////////////
typedefDict["DFITCConfirmMarkType"] = "int"
#确认
defineDict["DFITC_CON_CONFIRM"] = 2


#/////////////////////////////////////////////////////////
#DFITCStanAddrType:备用地址数据类型
#/////////////////////////////////////////////////////////
typedefDict["DFITCStanAddrType"] = "string"


#/////////////////////////////////////////////////////////
#DFITCCapControlModeType:资金控制方式数据类型
#/////////////////////////////////////////////////////////
typedefDict["DFITCCapControlModeType"] = "long"
#盯市盈亏可用 
defineDict["DFITC_PPL_USABLE"] = 2
#平仓资金T+1可用 
defineDict[""] = 4
#平仓保证金可取 
defineDict[""] = 8
#本日盈亏可取 
defineDict[""] = 16
#取后权益大于本日总入金 
defineDict[""] = 32
#平仓盈亏可取 
defineDict[""] = 128
#权利金收入可取 
defineDict[""] = 256


#/////////////////////////////////////////////////////////
#DFITCArchRatioType:转存比例数据类型
#/////////////////////////////////////////////////////////
typedefDict["DFITCArchRatioType"] = "float"


#/////////////////////////////////////////////////////////
#DFITCSettlementBillTradeType:汇总标志数据类型
#/////////////////////////////////////////////////////////
typedefDict["DFITCSettlementBillTradeType"] = "int"
#汇总成交明细
defineDict["DFITC_MATCHDETAIL"] = 2
#汇总持仓盈亏
defineDict["DFITC_OPGAL"] = 4
#汇总平仓盈亏
defineDict["DFITC_OFGAL"] = 8


#/////////////////////////////////////////////////////////
#DFITCFilesFlagType:档案类型数据类型
#/////////////////////////////////////////////////////////
typedefDict["DFITCFilesFlagType"] = "int"
#成交明细打印
defineDict["DFITC_PRINT_MATCHDETAIL"] = 4
#持仓盈亏打印 
defineDict["DFITC_PRINT_OPGAL"] = 8
#平仓盈亏打印 
defineDict["DFITC_PRINT_OFGAL"] = 16
#资金出入打印
defineDict["DFITC_PRINT_ACCESSFUNDS"] = 32
#追保声明打印
defineDict["DFITC_PRINT_ADDMARGIN"] = 64


#/////////////////////////////////////////////////////////
#DFITCSoftwareVendorIDType:软件供应商编号数据类型
#/////////////////////////////////////////////////////////
typedefDict["DFITCSoftwareVendorIDType"] = "string"


#/////////////////////////////////////////////////////////
#DFITCProductOnlineCountType:产品在线数量数据类型
#/////////////////////////////////////////////////////////
typedefDict["DFITCProductOnlineCountType"] = "long"


#/////////////////////////////////////////////////////////
#DFITCBrokerInfoType:期货公司名称数据类型
#/////////////////////////////////////////////////////////
typedefDict["DFITCBrokerInfoType"] = "string"


#/////////////////////////////////////////////////////////
#DFITCProductIDType:产品编号数据类型
#/////////////////////////////////////////////////////////
typedefDict["DFITCProductIDType"] = "string"


#/////////////////////////////////////////////////////////
#DFITCRequestIDType:请求ID数据类型
#/////////////////////////////////////////////////////////
typedefDict["DFITCRequestIDType"] = "long"


#/////////////////////////////////////////////////////////
#DFITCCustomCategoryType:自定义类别数据类型
#/////////////////////////////////////////////////////////
typedefDict["DFITCCustomCategoryType"] = "string"


#/////////////////////////////////////////////////////////
#DFITCReservedType:预留字段数据类型
#/////////////////////////////////////////////////////////
typedefDict["DFITCReservedType"] = "int"


#/////////////////////////////////////////////////////////
#DFITCNoticeType:消息数据类型
#/////////////////////////////////////////////////////////
typedefDict["DFITCNoticeType"] = "short"
#系统广播
defineDict["DFITC_SYS_BROADCAST_MSG"] = 1
#指定客户
defineDict["DFITC_ACCOUNT_ID_MSG"] = 2


#/////////////////////////////////////////////////////////
#DFITCTradingSegmentSNType:交易阶段编号数据类型
#/////////////////////////////////////////////////////////
typedefDict["DFITCTradingSegmentSNType"] = "int"


#///////////////////////////////////////////
#DFITCExtOrderType:算法单类型数据类型
#///////////////////////////////////////////
typedefDict["DFITCExtOrderType"] = "int"

#预埋单
defineDict["DFITC_YMORDER"] = 1
#条件单
defineDict["DFITC_TJORDER"] = 2
#跨期套利订单
defineDict["DFITC_KQTLDD"] = 3
#跨品种套利订单
defineDict["DFITC_KPZTLDD"] = 4
#蝶式套利订单
defineDict["DFITC_DSTLDD"] = 5
#自定义套利订单(暂不支持)
defineDict["DFITC_ZDYTLDD"] = 6

#///////////////////////////////////////////
#DFITCTriggerTime:触发时间数据类型
#///////////////////////////////////////////
typedefDict["DFITCTriggerTime"] = "string"


#///////////////////////////////////////////
#DFITCPriceReference:价格参照数据类型
#///////////////////////////////////////////
typedefDict["DFITCPriceReference"] = "int"

#参照最新价
defineDict["DFITC_REF_LASTPRICE"] = 0
#参照买一价
defineDict["DFITC_REF_BIDPRICE"] = 1
#参照卖出价
defineDict["DFITC_REF_ASKPRICE"] = 2

#///////////////////////////////////////////
#DFITCCompareFlag:比较标志数据类型
#///////////////////////////////////////////
typedefDict["DFITCCompareFlag"] = "int"

#大于
defineDict["DFITC_CF_GREATER"] = 0
#大于等于
defineDict["DFITC_CF_NOTLESS"] = 1
#小于
defineDict["DFITC_CF_LESS"] = 2
#小于等于
defineDict["DFITC_CF_NOTGREATER"] = 3

#///////////////////////////////////////////
#DFITCOvernightFlag:隔夜标志数据类型
#///////////////////////////////////////////
typedefDict["DFITCOvernightFlag"] = "int"

#隔夜
defineDict["DFITC_OVERNIGHT"] = 1
#不隔夜
defineDict["DFITC_NOT_OVERNIGHT"] = 2

#///////////////////////////////////////////
#DFITCArbitragePrice:套利价格数据类型
#///////////////////////////////////////////
typedefDict["DFITCArbitragePrice"] = "float"


#///////////////////////////////////////////
#DFITCExtTriggerCond:触发条件数据类型
#///////////////////////////////////////////
typedefDict["DFITCExtTriggerCond"] = "int"

#价格触发
defineDict["DFITC_TRIGGER_PRICE"] = 0
#时间触发
defineDict["DFITC_TRIGGER_TIME"] = 1


#/////////////////////////////////////////////////////////
#DFITCInstrumentMaturityType:合约最后交易日
#/////////////////////////////////////////////////////////
typedefDict["DFITCInstrumentMaturityType"] = "string"


#/////////////////////////////////////////////////////////
#DFITCInstrumenExpirationDateType:合约到期日
#/////////////////////////////////////////////////////////
typedefDict["DFITCInstrumenExpirationDateType"] = "string"


#/////////////////////////////////////////////////////////
#DFITCAdjustmentInfoType:组合或对锁的保证金调整信息
#格式:[合约代码,买卖标志,投资类别,调整金额;]
#/////////////////////////////////////////////////////////
typedefDict["DFITCAdjustmentInfoType"] = "string"


#/////////////////////////////////////////////////////////
#DFITCQuoteIDType:询价编号
#/////////////////////////////////////////////////////////
typedefDict["DFITCQuoteIDType"] = "string"


#/////////////////////////////////////////////////////////
#DFITCSourceType:来源
#/////////////////////////////////////////////////////////
typedefDict["DFITCSourceType"] = "short"

#会员
defineDict["DFITC_SOURCE_MEMBER"] = 0
#交易所
defineDict["DFITC_SOURCE_EXCHANGE"] = 1


#/////////////////////////////////////////////////////////
#DFITCSeatCodeType:席位代码
#/////////////////////////////////////////////////////////
typedefDict["DFITCSeatCodeType"] = "string"


#/////////////////////////////////////////////////////////
#DFITCCloseIDType:平仓执行单号
#/////////////////////////////////////////////////////////
typedefDict["DFITCCloseIDType"] = "string"


#/////////////////////////////////////////////////////////
#DFITCEntrusTellerType:委托柜员
#/////////////////////////////////////////////////////////
typedefDict["DFITCEntrusTellerType"] = "string"


#/////////////////////////////////////////////////////////
#DFITCStayTimeType：停留时间数据类型
#/////////////////////////////////////////////////////////
typedefDict["DFITCStayTimeType"] = "int"


#/////////////////////////////////////////////////////////
#DFITCComputeModeType：计算方式数据类型
#/////////////////////////////////////////////////////////
typedefDict["DFITCComputeModeType"] = "int"
#绝对数值计算
defineDict["DFITC_ABSOLUTE_VALUE_COMPUTE"] = 0
#交易所保证金标准基础上浮动
defineDict["DFITC_EXCHANGE_MARGIN_BASIS_FLOAT"] = 1
#交易所保证金结果基础上浮动
defineDict["DFITC_EXCHANGE_MARGIN_RESULT_FLOAT"] = 2
#期货保证金标准基础上浮动
defineDict["DFITC_FUTURES_MARGIN_BASIS_FLOAT"] = 3


#//////////////////////////////////////////////////////////////////////
#DFITCPriceNoteType:期权保证金计算方式
#//////////////////////////////////////////////////////////////////////
typedefDict["DFITCPriceNoteType"] = "int"
#按照昨结算价计算
defineDict["DFITC_CALC_BY_PRESETTLEMENT"] = 1
#按照最新价计算
defineDict["DFITC_CALC_BY_LASTPRICE"] = 2

#//////////////////////////////////////////////////////////////////////
#DFITCLargeMarginDirectType:大边保证金方向数据类型
#//////////////////////////////////////////////////////////////////////
typedefDict["DFITCLargeMarginDirectType"] = "string"

#//////////////////////////////////////////////////////////////////////
#DFITCBankIDType:银行代码类型
#//////////////////////////////////////////////////////////////////////
typedefDict["DFITCBankIDType"] = "string"

#//////////////////////////////////////////////////////////////////////
#DFITCBankNameType:银行名称类型
#//////////////////////////////////////////////////////////////////////
typedefDict["DFITCBankNameType"] = "string"

#//////////////////////////////////////////////////////////////////////
#DFITCBankSerialType:银行流水号类型
#//////////////////////////////////////////////////////////////////////
typedefDict["DFITCBankSerialType"] = "string"

#//////////////////////////////////////////////////////////////////////
#DFITCSerialType:流水号类型
#//////////////////////////////////////////////////////////////////////
typedefDict["DFITCSerialType"] = "int"

#//////////////////////////////////////////////////////////////////////
#DFITCBankAccountType:银行账户类型
#//////////////////////////////////////////////////////////////////////
typedefDict["DFITCBankAccountType"] = "string"

#//////////////////////////////////////////////////////////////////////
#DFITCFutureSerialType:期货公司流水号类型
#//////////////////////////////////////////////////////////////////////
typedefDict["DFITCFutureSerialType"] = "int"

#//////////////////////////////////////////////////////////////////////
#DFITCDigestType:摘要类型
#//////////////////////////////////////////////////////////////////////
typedefDict["DFITCDigestType"] = "string"

#//////////////////////////////////////////////////////////////////////
#DFITCBankAccTypeType是一个银行帐号类型类型
#//////////////////////////////////////////////////////////////////////
#银行存折
defineDict["DFITC_BAT_BankBook"] = '1'
#储蓄卡
defineDict["DFITC_BAT_SavingCard"] = '2'
#信用卡
defineDict["DFITC_BAT_CreditCard"] = '3'
typedefDict["DFITCBankAccTypeType"] = "char"

#//////////////////////////////////////////////////////////////////////
#DFITCTransferStatusType:转账交易状态类型
#//////////////////////////////////////////////////////////////////////
#正常
defineDict["DFITC_TRFS_Normal"] = '0'
#被冲正
defineDict["DFITC_TRFS_Repealed"] = '1'
typedefDict["DFITCTransferStatusType"] = "char"

#//////////////////////////////////////////////////////////////////////
#DFITCTransferType:银期转账业务类型
#//////////////////////////////////////////////////////////////////////
typedefDict["DFITCTransferType"] = "int"

#//////////////////////////////////////////////////////////////////////
#DFITCTransferType:银期转账处理结果类型
#//////////////////////////////////////////////////////////////////////
typedefDict["DFITCProcResultType"] = "int"
#成功
defineDict["DFITC_PROC_SUCCESS"] = 0
#失败
defineDict["DFITC_PROC_FAIL"] = 1
#等待回执
defineDict["DFITC_PROC_WAIT_RTN"] = 2


#//////////////////////////////////////////////////////////////////////
#DFITCApplyNumberType:银期转账申请号类型
#//////////////////////////////////////////////////////////////////////
typedefDict["DFITCApplyNumberType"] = "int"



#//////////////////////////////////////////////////////////////////////
#DFITCImpliedVolatilityType:隐含波动率类型
#//////////////////////////////////////////////////////////////////////
typedefDict["DFITCImpliedVolatilityType"] = "float"

#//////////////////////////////////////////////////////////////////////
#DFITCOptionComputationType:期权计算数据类型
#//////////////////////////////////////////////////////////////////////
typedefDict["DFITCOptionComputationType"] = "float"

#/////////////////////////////////////////////////////////
#DFITCFunctionIDType:行情扩展功能号
#/////////////////////////////////////////////////////////
typedefDict["DFITCFunctionIDType"] = "string"

#/////////////////////////////////////////////////////////
#DFITCExtMarketDataType:行情扩展功能号
#/////////////////////////////////////////////////////////
typedefDict["DFITCExtMarketDataType"] = "string"



#//////////////////////////////////////////////////////////////////////
#DFITCExchangeStatusType:交易所状态数据类型
#//////////////////////////////////////////////////////////////////////
typedefDict["DFITCExchangeStatusType"] = "int"
#开盘前
defineDict["DFITC_IS_BEFORETRADING"] = 0
#非交易
defineDict["DFITC_IS_NOTRADING"] = 1
#连续交易
defineDict["DFITC_IS_CONTINOUS"] = 2
#集合竞价报单
defineDict["DFITC_IS_AUCTIONORDERING"] = 3
#集合竞价价格平衡
defineDict["DFITC_IS_AUCTIONBALANCE"] = 4
#集合竞价撮合
defineDict["DFITC_IS_AUCTIONMATCH"] = 5
#收盘
defineDict["DFITC_IS_CLOSED"] = 6


#//////////////////////////////////////////////////////////////////////
#DFITCPositionDateType:持仓日期类型
#//////////////////////////////////////////////////////////////////////
typedefDict["DFITCPositionDateType"] = "int"
defineDict["DFITC_PSD_TODAY"] = 1
defineDict["DFITC_PSD_HISTORY"] = 2

