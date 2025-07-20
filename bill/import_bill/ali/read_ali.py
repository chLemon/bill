from domain.TradeRecord import TradeRecord
from datetime import datetime

BILL_TYPE = "支付宝"

DATA_DIR_PATH = "data/支付宝"


def read_ali_file(file):
    """
    读取支付宝账单文件
    return: 账单记录列表，账单时间区间
    """
    with open(file, 'r', encoding='gbk') as f:
        lines = f.readlines()
        trade_record_str_list = lines[25:]
        time = lines[4]
        start_time = datetime.strptime(time[6:25], "%Y-%m-%d %H:%M:%S")
        end_time = datetime.strptime(time[36:55], "%Y-%m-%d %H:%M:%S")
    return [TradeRecord.from_ali_str(trade_record_str, BILL_TYPE) for trade_record_str in trade_record_str_list], start_time, end_time
