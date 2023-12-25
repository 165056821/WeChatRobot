from datetime import datetime
import pytz
from tortoise.fields import DatetimeField

# 定义一个CustomDatetimeField类，继承自DatetimeField
class CustomDatetimeField(DatetimeField):
    # 重写to_python_value方法，用于将传入的值转换为python值
    def to_python_value(self, value):
        # 调用父类的to_python_value方法，将传入的值转换为python值
        value = super().to_python_value(value)
        # 如果传入的值为None或者已经转换为CustomDateTime类型，则直接返回
        if value is None or isinstance(value, CustomDateTime):
            return value
        # 否则，将传入的值转换为CustomDateTime类型，并返回
        return CustomDateTime(value.year, value.month, value.day, value.hour, value.minute, value.second, value.microsecond, value.tzinfo)


# 定义一个CustomDateTime类，继承自datetime
class CustomDateTime(datetime):
    # 定义一个get_beijing_time方法，返回 Beijing Time
    def get_beijing_time(self):
        # 定义Beijing时区
        beijing_tz = pytz.timezone('Asia/Shanghai')
        # 将datetime对象转换为UTC时间，并转换为Beijing时区
        return self.replace(tzinfo=pytz.utc).astimezone(beijing_tz)
