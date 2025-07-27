from pathlib import Path
from datetime import datetime
from dateutil.relativedelta import relativedelta
from pypdf import PdfReader
import re

from domain import PufaCreditTradeRecord

BILL_TYPE = "浦发银行信用卡"

DATA_DIR_PATH = "data/浦发银行信用卡"

# 还款日，包含在当前月的账单中
STATEMENT_DUE_DATE = 20


def parse_trade_record(match: str) -> PufaCreditTradeRecord:
    """
    解析 浦发银行信用卡 交易记录字符串，返回 PufaCreditTradeRecord 对象
    """
    is_expense = match[2].startswith("-")

    return PufaCreditTradeRecord(
        trade_time=match[0],
        trade_target=match[1],
        product="",
        income_or_expense="收入" if is_expense else "支出",
        amount=match[2][1:] if is_expense else match[2],
        bill_type=BILL_TYPE,
        trade_no=str(match),
    )


def read_pufa_bank_credit_file(file: Path):
    """
    读取 浦发银行信用卡 账单文件
    """
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    pattern = r"(\d{8}) \d{8} (.*) \d{4} ￥([-]*\d+\.\d+).*"
    matches = re.findall(pattern, text)

    # 某个月的账单，假设还款日为5日，是从上个月的6日00:00:00，到这个月的5日23:59:59
    due_date = datetime.strptime(
        file.name[:6] + str(STATEMENT_DUE_DATE), "%Y%m%d"
    )
    end_time = due_date.replace(hour=23, minute=59, second=59)
    start_time = due_date - relativedelta(months=1) + relativedelta(days=1)

    return (
        [parse_trade_record(match) for match in matches],
        start_time,
        end_time,
    )
