from domain.GroupData import GroupData


def group(all_trade_records):
    """
    将所有的交易记录按年和月分组
    :param all_trade_records: 所有的交易记录
    :return: 年份到月份到交易记录的映射
    """
    year_to_month_to_trade_records = {}
    for trade_record in all_trade_records:
        year = trade_record.trade_time.year
        month = trade_record.trade_time.month
        if year not in year_to_month_to_trade_records:
            year_to_month_to_trade_records[year] = {}
        if month not in year_to_month_to_trade_records[year]:
            year_to_month_to_trade_records[year][month] = []
        year_to_month_to_trade_records[year][month].append(trade_record)
    return year_to_month_to_trade_records


def do_statistic(trade_records):
    """统计分析

    Args:
        trade_records (_type_): _description_

    Returns:
        _type_: _description_
    """
    return None


def group_and_statistic(all_trade_records):
    """
    将所有的交易记录按年和月分组，并进行统计分析
    :param all_trade_records: 所有的交易记录
    :return: 年份到月份到交易记录的映射
    """
    year_to_month_to_trade_records = group(all_trade_records)
    year_to_month_to_group_data = {}
    for year, month_to_trade_records in year_to_month_to_trade_records.items():
        if year not in year_to_month_to_group_data:
            year_to_month_to_group_data[year] = {}
        for month, trade_records in month_to_trade_records.items():
            statistic = do_statistic(trade_records)
            year_to_month_to_group_data[year][month] = GroupData.monthData(
                month=month, trade_records=trade_records, statistic=statistic)
    return year_to_month_to_group_data