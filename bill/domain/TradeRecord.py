from datetime import datetime
from dataclasses import dataclass, field

@dataclass
class TradeRecord:
    """
    交易记录类

    Attributes:
        trade_time (datetime): 交易时间
        trade_type (str): 交易类型
        trade_target (str): 交易对方
        trade_target_account (str): 交易对方账号，可选
        product (str): 商品
        income_or_expense (str): 收/支
        amount (str): 金额(元)
        pay_type (str): 支付方式
        status (str): 当前状态
        trade_no (str): 交易单号
        merchant_no (str): 商户单号
        remark (str): 备注
        bill_type (str): 订单类型
        sub_record (TradeRecord): 子订单，可选
    """
    trade_time: str = field(metadata={"desc": "交易时间"})
    trade_type: str = field(metadata={"desc": "交易类型"})
    trade_target: str = field(metadata={"desc": "交易对方"})
    trade_target_account: str = field(default=None, metadata={"desc": "交易对方账号"})
    product: str = field(metadata={"desc": "商品"})
    income_or_expense: str = field(metadata={"desc": "收/支"})
    amount: str = field(metadata={"desc": "金额(元)"})
    pay_type: str = field(metadata={"desc": "支付方式"})
    status: str = field(metadata={"desc": "当前状态"})
    trade_no: str = field(metadata={"desc": "交易单号"})
    merchant_no: str = field(metadata={"desc": "商户单号"})
    remark: str = field(metadata={"desc": "备注"})
    bill_type: str = field(metadata={"desc": "订单类型"})

    def __init__(
        self,
        trade_time: str,
        trade_type: str,
        trade_target: str,
        product: str,
        income_or_expense: str,
        amount: str,
        pay_type: str,
        status: str,
        trade_no: str,
        merchant_no: str,
        remark: str,
        bill_type: str,
        trade_target_account: str = None,
    ):
        self.trade_time = datetime.strptime(
            trade_time, "%Y-%m-%d %H:%M:%S")                # 交易时间
        self.trade_type = trade_type                        # 交易类型
        self.trade_target = trade_target                    # 交易对方
        self.trade_target_account = trade_target_account    # 交易对方账号
        self.product = product                              # 商品
        self.income_or_expense = income_or_expense          # 收/支
        self.amount = amount                                # 金额(元)
        self.pay_type = pay_type                            # 支付方式
        self.status = status                                # 当前状态
        self.trade_no = trade_no                            # 交易单号
        self.merchant_no = merchant_no                      # 商户单号
        self.remark = remark                                # 备注
        self.bill_type = bill_type                          # 订单类型

    def from_wx_str(trade_record_str: str, bill_type: str):
        """
        从微信字符串中解析交易记录
        交易时间, 交易类型,交易对方,商品,收/支,金额(元),支付方式,当前状态,交易单号,商户单号,备注
        2025-05-06 16:31:56,商户消费,便利蜂,便利蜂购物,支出,¥9.80,零钱,支付成功,42000026xxx,2130xxx,/
        """
        # 解析字符串
        fields = trade_record_str.split(',')
        # 创建交易记录对象
        return TradeRecord(
            trade_time=fields[0].strip().strip('"'),
            trade_type=fields[1].strip().strip('"'),
            trade_target=fields[2].strip().strip('"'),
            product=fields[3].strip().strip('"'),
            income_or_expense=fields[4].strip().strip('"'),
            amount=fields[5].strip().strip('"'),
            pay_type=fields[6].strip().strip('"'),
            status=fields[7].strip().strip('"'),
            trade_no=fields[8].strip().strip('"'),
            merchant_no=fields[9].strip().strip('"'),
            remark=fields[10].strip().strip('"'),
            bill_type=bill_type,
        )

    def from_ali_str(trade_record_str: str, bill_type: str):
        """
        从支付宝字符串中解析交易记录
        交易时间,交易分类,交易对方,对方账号,商品说明,收/支,金额,收/付款方式,交易状态,交易订单号,商家订单号,备注,\n
        2025-05-04 22:11:22,餐饮美食,饿了么,e50***@alibaba-inc.com,小谷姐姐麻辣拌●麻辣烫(六佰本店)外卖订单,支出,13.07,浦发银行信用卡(xxxx),交易成功,20250504220xxx\t,13220600725050456510516307714\t,,\n
        """
        # 解析字符串
        fields = trade_record_str.split(',')
        # 创建交易记录对象
        return TradeRecord(
            trade_time=fields[0].strip().strip('"'),
            trade_type=fields[1].strip().strip('"'),
            trade_target=fields[2].strip().strip('"'),
            trade_target_account=fields[3].strip().strip('"'),
            product=fields[4].strip().strip('"'),
            income_or_expense=fields[5].strip().strip('"'),
            amount=fields[6].strip().strip('"'),
            pay_type=fields[7].strip().strip('"'),
            status=fields[8].strip().strip('"'),
            trade_no=fields[9].strip().strip('"'),
            merchant_no=fields[10].strip().strip('"'),
            remark=fields[11].strip().strip('"'),
            bill_type=bill_type
        )

    def __str__(self):
        return ', '.join(f"{k}={v}" for k, v in vars(self).items())
