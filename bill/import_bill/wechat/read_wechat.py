from datetime import datetime
from typing import List
import csv

from domain import WechatTradeRecord

BILL_TYPE = "微信"

DATA_DIR_PATH = "data/微信"


def parse_trade_record(trade_record: List["str"]) -> WechatTradeRecord:
    """
    解析微信交易记录字符串，返回 WechatTradeRecord 对象
    """
    return WechatTradeRecord(
        trade_time=trade_record[0].strip().strip('"'),
        trade_type=trade_record[1].strip().strip('"'),
        trade_target=trade_record[2].strip().strip('"'),
        product=trade_record[3].strip().strip('"'),
        income_or_expense=trade_record[4].strip().strip('"'),
        amount=trade_record[5].strip().strip('"').replace("¥", ""),
        pay_type=trade_record[6].strip().strip('"'),
        status=trade_record[7].strip().strip('"'),
        trade_no=trade_record[8].strip().strip('"'),
        merchant_no=trade_record[9].strip().strip('"'),
        remark=trade_record[10].strip().strip('"'),
        bill_type=BILL_TYPE,
    )


def read_wx_file(file):
    """
    读取微信账单文件
    """
    with open(file, "r", encoding="utf-8") as f:
        csv_reader_res = list(csv.reader(f))
        trade_record_lines = csv_reader_res[17:]
        time = csv_reader_res[2][0]
        start_time = datetime.strptime(time[6:25], "%Y-%m-%d %H:%M:%S")
        end_time = datetime.strptime(time[33:52], "%Y-%m-%d %H:%M:%S")
    return (
        [parse_trade_record(trade_record) for trade_record in trade_record_lines],
        start_time,
        end_time,
    )
