from domain import AliTradeRecord
from datetime import datetime

BILL_TYPE = "支付宝"

DATA_DIR_PATH = "data/支付宝"


def parse_trade_record(trade_record_str: str) -> AliTradeRecord:
    """
    解析支付宝交易记录字符串，返回 AliTradeRecord 对象
    """
    fields = trade_record_str.split(",")
    return AliTradeRecord(
        trade_time=fields[0].strip().strip('"'),
        trade_type=fields[1].strip().strip('"'),
        trade_target=fields[2].strip().strip('"'),
        target_account=fields[3].strip().strip('"'),
        product=fields[4].strip().strip('"'),
        income_or_expense=fields[5].strip().strip('"'),
        amount=fields[6].strip().strip('"'),
        pay_type=fields[7].strip().strip('"'),
        status=fields[8].strip().strip('"'),
        trade_no=fields[9].strip().strip('"'),
        merchant_no=fields[10].strip().strip('"'),
        remark=fields[11].strip().strip('"'),
        bill_type=BILL_TYPE,
    )


def read_ali_file(file):
    """
    读取支付宝账单文件
    return: 账单记录列表，账单时间区间
    """
    with open(file, "r", encoding="gbk") as f:
        lines = f.readlines()
        trade_record_str_list = lines[25:]
        time = lines[4]
        start_time = datetime.strptime(time[6:25], "%Y-%m-%d %H:%M:%S")
        end_time = datetime.strptime(time[36:55], "%Y-%m-%d %H:%M:%S")
    return (
        [
            parse_trade_record(trade_record_str)
            for trade_record_str in trade_record_str_list
        ],
        start_time,
        end_time,
    )
