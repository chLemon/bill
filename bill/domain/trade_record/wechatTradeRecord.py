from .baseTradeRecord import BaseTradeRecord
from pydantic import Field


class WechatTradeRecord(BaseTradeRecord):
    """
    微信交易记录类

    交易时间,交易类型,交易对方,商品,收/支,金额(元),支付方式,当前状态,交易单号,商户单号,备注
    2025-01-01 01:01:01,商户消费,便利蜂,便利蜂购物,支出,¥9.80,零钱,支付成功,xxxx,xxxx,/


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
            trade_no (str): 交易单号
        wechat specific fields:
            trade_type (str): 交易类型
            pay_type (str): 支付方式
            status (str): 当前状态
            merchant_no (str): 商户单号
            remark (str): 备注
    """

    trade_type: str = Field(description="交易类型")
    pay_type: str = Field(description="支付方式")
    status: str = Field(description="当前状态")
    merchant_no: str = Field(description="商户单号")
    remark: str = Field(description="备注")