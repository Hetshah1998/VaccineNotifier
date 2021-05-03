import logging
from datetime import datetime,timedelta


def get_5days():
    days = []
    days.append("{:%d-%m-%Y}".format(datetime.now()))

    for i in range(4):
        days.append("{:%d-%m-%Y}".format(datetime.now() + timedelta(days=(i+1))))
    return days


def init_logging():
    logging.basicConfig(format='%(name)s- %(levelname)s -%(message)s', level="INFO")
