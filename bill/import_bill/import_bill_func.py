from pathlib import Path
from datetime import datetime, timedelta
from .billType import BillType


def read_all_bills():
    """
    读取所有账单
    :return: 所有账单记录，账单时间区间
    """
    all_trade_records = []
    bill_time_range = {}
    # 读取所有类型的账单数据
    for bill in BillType:
        trade_records, times = read_trade_records(bill.read_func, Path(bill.data_path))
        trade_records.sort(key=lambda x: x.trade_time)
        all_trade_records.extend(trade_records)
        bill_time_range[bill.bill_type] = times
    return all_trade_records, bill_time_range


def read_trade_records(read_func, dir_path: Path):
    """
    读取某个目录下的所有账单文件
    :param read_func: 读取函数
    :param dir_path: 目录路径
    :return: 账单记录列表，账单时间区间
    """
    files = [file for file in Path(dir_path).iterdir() if file.is_file() and file.suffix in ['.csv', '.xlsx', '.pdf', '.xls']]
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
    if (
        last_end.hour == 23
        and last_end.minute == 59
        and last_end.second == 59
        and last_end + timedelta(seconds=1) == next_start
    ):
        return True
    return False
