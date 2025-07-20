from enum import Enum
from import_bill.ali import read_ali_file, BILL_TYPE as ALIPAY_BILL_TYPE, DATA_DIR_PATH as ALIPAY_DATA_DIR_PATH
from import_bill.wechat import read_wx_file, BILL_TYPE as WECHAT_BILL_TYPE, DATA_DIR_PATH as WECHAT_DATA_DIR_PATH
from pathlib import Path


class Bill(Enum):
    WECHAT = (read_wx_file, WECHAT_DATA_DIR_PATH, WECHAT_BILL_TYPE)
    ALIPAY = (read_ali_file, ALIPAY_DATA_DIR_PATH, ALIPAY_BILL_TYPE)

    def __init__(self, read_func, data_path, bill_name):
        self.read_func = read_func
        self.bill_name = bill_name
        self.data_path = Path(__file__).resolve().parent.parent.parent / data_path
