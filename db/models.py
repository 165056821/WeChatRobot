from tortoise.models import Model
from tortoise import fields

from db.CustomDatetimeField import CustomDatetimeField
from db.timezone_converter import timezone_converter


class Log(Model):
    id = fields.IntField(pk=True, description="主键")
    message = fields.TextField(description="日志信息")
    level = fields.CharField(max_length=10, description="日志级别")
    created_at = fields.DatetimeField(auto_now_add=True, use_tz=False, description="创建时间")
    updated_at = CustomDatetimeField(auto_now=True, description="更新时间")
    updated_at2 = CustomDatetimeField(auto_now=True, description="更新时间")
    source = fields.CharField(max_length=50, null=True, description="日志来源")
    extra_info = fields.JSONField(null=True, description="额外信息")

    @property
    @timezone_converter()
    def created_at_local(self):
        return self.created_at

    @property
    @timezone_converter()
    def updated_at_local(self):
        return self.updated_at
    class Meta:
        table = "log"
        table_description = "日志表"

