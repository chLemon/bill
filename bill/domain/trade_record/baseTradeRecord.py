from datetime import datetime
from pydantic import BaseModel, Field, field_validator
from enum import Enum


class IncomeOrExpense(Enum):
    INCOME = "收入"
    EXPENSE = "支出"
    NONE1 = "不计收支"
    NONE2 = "/"


class BaseTradeRecord(BaseModel):
    """
    基础交易记录类

    Attributes:
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

    trade_time: datetime = Field(description="交易时间")
    trade_target: str = Field(description="交易对方")
    product: str = Field(description="商品")
    income_or_expense: "IncomeOrExpense" = Field(description="收/支")
    amount: float = Field(description="金额(元)")
    promotion_or_refund_records: list["BaseTradeRecord"] = Field(
        default_factory=list, description="优惠/退款记录"
    )
    related_records: list["BaseTradeRecord"] = Field(
        default_factory=list,
        description="关联记录（主要是如微信支付对应的银行支付记录）",
    )
    bill_type: str = Field(description="账单类型，是来自微信还是支付宝等")
    trade_no: str = Field(default="", description="交易单号")

    @field_validator("trade_time")
    def make_naive(cls, v):
        # 去掉时区信息
        return v.replace(tzinfo=None)
