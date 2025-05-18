from pathlib import Path
from datetime import datetime

from domain.TradeRecord import TradeRecord

BILL_TYPE = "微信"


def read_wx_file(file):
    """
    读取微信账单文件
    """
    with open(file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        trade_record_str_list = lines[17:]
        time = lines[2]
        start_time = datetime.strptime(time[6:25], "%Y-%m-%d %H:%M:%S")
        end_time = datetime.strptime(time[33:52], "%Y-%m-%d %H:%M:%S")
    return [TradeRecord.from_wx_str(trade_record_str, BILL_TYPE) for trade_record_str in trade_record_str_list], start_time, end_time
