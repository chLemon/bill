from .Statistic import Statistic


class SheetData:
    """
    sheet页内的数据

    Attributes:
        sheet_name (str): sheet页名称
        trade_record_title (list): 交易记录标题
        trade_records (list): 交易记录列表
        statistic (Statistic): 统计分析结果
    """

    def __init__(self, sheet_name: str, trade_record_title: list, trade_records: list, statistic: 'Statistic'):
        self.sheet_name = sheet_name
        self.trade_record_title = trade_record_title
        self.trade_records = trade_records
        self.statistic = statistic

    def monthData(month, trade_records, statistic):
        """
        每月的交易数据
        :param year: 年份
        :param month: 月份
        :param trade_records: 交易记录列表
        :return: 每月的交易数据
        """
        return SheetData(sheet_name=str(month) + "月账单",
                         # todo 这里做成  商品 product 这样的 tuple
                         trade_record_title=[],
                         trade_records=trade_records,
                         statistic=statistic)
