import pytz


def datetime_utc_to_local(date_time):
    return date_time.replace(tzinfo=pytz.timezone('UTC')).astimezone(pytz.timezone('Asia/Shanghai'))
