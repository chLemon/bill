from pathlib import Path
from datetime import datetime, timedelta


def read_trade_records(read_func, dir_path: Path):
    """
    读取某个目录下的所有账单文件
    :param read_func: 读取函数
    :param dir_path: 目录路径
    :return: 账单记录列表，账单时间区间
    """
    files = [file for file in Path(dir_path).iterdir() if file.is_file()]
    trade_record_list = []
    time_list = []
    distinct_set = set()
    for file in files:
        file_trade_record_list, start_time, end_time = read_func(file)
        distinct_merge(trade_record_list, distinct_set, file_trade_record_list)
        time_list.append((start_time, end_time))
    time_list = merge_time_range(time_list)
    return trade_record_list, time_list

def distinct_merge(all_list, distinct_set, new_list):
    for item in new_list:
        if item.trade_no not in distinct_set:
            all_list.append(item)
            distinct_set.add(item.trade_no)

def merge_time_range(time_list):
    """
    合并时间区间
    :param time_list: 时间区间列表
    :return: 合并后的时间区间列表
    """
    if not time_list:
        return []
    time_list.sort(key=lambda x: x[0])
    merged_time_list = [time_list[0]]
    for start_time, end_time in time_list[1:]:
        last_start, last_end = merged_time_list[-1]
        if time_consistency_check(last_end, start_time):
            merged_time_list[-1] = (last_start, max(last_end, end_time))
        else:
            merged_time_list.append((start_time, end_time))
    return merged_time_list


def time_consistency_check(last_end: datetime, next_start: datetime):
    if last_end >= next_start:
        return True
    if last_end.hour == 23 and last_end.minute == 59 and last_end.second == 59 and last_end + timedelta(seconds=1) == next_start:
        return True
    return False


class TradeRecord:
    """
    交易记录类

    Attributes:
        trade_time (str): 交易时间
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
        sub_record (TradeRecord): 子订单，可选
        bill_type (str): 订单类型
    交易时间,交易类型,交易对方,商品,收/支,金额(元),支付方式,当前状态,交易单号,商户单号,备注
    """

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
        self.trade_time = trade_time      # 交易时间
        self.trade_type = trade_type      # 交易类型
        self.trade_target = trade_target  # 交易对方
        self.trade_target_account = trade_target_account  # 交易对方账号
        self.product = product            # 商品
        self.income_or_expense = income_or_expense  # 收/支
        self.amount = amount              # 金额(元)
        self.pay_type = pay_type      # 支付方式
        self.status = status              # 当前状态
        self.trade_no = trade_no          # 交易单号
        self.merchant_no = merchant_no    # 商户单号
        self.remark = remark              # 备注
        self.bill_type = bill_type              # 订单类型

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
