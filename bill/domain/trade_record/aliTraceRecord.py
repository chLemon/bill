from .baseTradeRecord import BaseTradeRecord
from pydantic import Field


class AliTradeRecord(BaseTradeRecord):
    """
    支付宝交易记录类

    交易时间,交易分类,交易对方,对方账号,商品说明,收/支,金额,收/付款方式,交易状态,交易订单号,商家订单号,备注,
    2025-01-01 00:00:00,餐饮美食,饿了么,e50***@alibaba-inc.com,麻辣烫外卖订单,支出,13.07,浦发银行信用卡(xxxx),交易成功,xxxx,xxxx,,


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
            trade_no (str): 交易订单号
        ali specific fields:
            trade_type (str): 交易分类
            target_account (str): 对方账号
            pay_type (str): 收/付款方式
            status (str): 交易状态
            merchant_no (str): 商家订单号
            remark (str): 备注
    """

    trade_type: str = Field(description="交易分类")
    target_account: str = Field(description="对方账号")
    pay_type: str = Field(description="收/付款方式")
    status: str = Field(description="交易状态")
    merchant_no: str = Field(description="商家订单号")
    remark: str = Field(description="备注")
