from TradeRecord import TradeRecord
from pathlib import Path

def read_wechat_bill(dir_path: Path):
    """
    读取某个目录下的所有微信账单文件
    """
    files = [file for file in Path(dir_path).iterdir() if file.is_file()]
    trade_record_list = []
    for file in files:
        trade_record_list.extend(read_wx_file(file))
    return trade_record_list

def read_wx_file(file):
    """
    读取微信账单文件
    """
    with open(file, 'r', encoding='utf-8') as f:
        trade_record_str_list = f.readlines()[17:]
    return [TradeRecord.from_str(trade_record_str) for trade_record_str in trade_record_str_list]
