import pytz
import time
from datetime import datetime


def datetime_utc_to_local(date_time_utc=None):
    if date_time_utc is None:
        date_time_utc = datetime.utcnow()

    return date_time_utc.replace(tzinfo=pytz.timezone('UTC')).astimezone(pytz.timezone('Asia/Shanghai'))


def datetime_local_timestamp(date_time_utc=None):
    t = datetime_utc_to_local(date_time_utc).timestamp()
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(t))+f'.{int((t-int(t))*1000):03d}'


def datetime_utc_iso8601(date_time_utc=None):
    if date_time_utc is None:
        date_time_utc = datetime.utcnow()
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.localtime(date_time_utc.timestamp()))
