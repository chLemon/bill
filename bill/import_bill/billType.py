from enum import Enum
from pathlib import Path

from .ali import (
    read_ali_file,
    BILL_TYPE as ALIPAY_BILL_TYPE,
    DATA_DIR_PATH as ALIPAY_DATA_DIR_PATH,
)
from .wechat import (
    read_wx_file,
    BILL_TYPE as WECHAT_BILL_TYPE,
    DATA_DIR_PATH as WECHAT_DATA_DIR_PATH,
)
from .pufa_bank_credit import (
    read_pufa_bank_credit_file,
    BILL_TYPE as PUFA_CREDIT_BILL_TYPE,
    DATA_DIR_PATH as PUFA_CREDIT_DATA_DIR_PATH,
)


class BillType(Enum):
    WECHAT = (read_wx_file, WECHAT_DATA_DIR_PATH, WECHAT_BILL_TYPE)
    ALIPAY = (read_ali_file, ALIPAY_DATA_DIR_PATH, ALIPAY_BILL_TYPE)
    PUFA_CREDIT = (read_pufa_bank_credit_file, PUFA_CREDIT_DATA_DIR_PATH, PUFA_CREDIT_BILL_TYPE)

    def __init__(self, read_func, data_path, bill_type):
        self.read_func = read_func
        self.bill_type = bill_type
        self.data_path = Path(__file__).resolve().parent.parent.parent / data_path
