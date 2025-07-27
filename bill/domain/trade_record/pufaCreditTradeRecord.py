from .baseTradeRecord import BaseTradeRecord, field_validator
from pydantic import Field


class PufaCreditTradeRecord(BaseTradeRecord):
    """
    浦发银行信用卡交易记录类

    Attributes:
        extends from BaseTradeRecord:
            trade_time (datetime): 交易时间
            trade_target (str): 交易对方
            product (str): 商品
            income_or_expense (IncomeOrExpense): 收入 / 支出
            amount (float): 金额(元)
            promotion_or_refund_records (list[BaseTradeRecord]): 优惠/退款记录
            related_records (list[BaseTradeRecord]): 关联记录（主要是如微信支付对应的银行支付记录）
            bill_type (str): 账单类型，是来自微信还是支付宝等
            trade_no (str): 交易单号，订单的唯一标识，如果没有需要生成一个
    """

