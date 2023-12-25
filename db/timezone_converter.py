# timezone_decorator.py

import pytz
from datetime import datetime

def timezone_converter(timezone='Asia/Shanghai'):
    def decorator(func):
        def wrapper(*args, **kwargs):
            utc_time = func(*args, **kwargs)
            if utc_time and isinstance(utc_time, datetime):
                tz = pytz.timezone(timezone)
                return utc_time.replace(tzinfo=pytz.utc).astimezone(tz)
            return utc_time
        return wrapper
    return decorator
