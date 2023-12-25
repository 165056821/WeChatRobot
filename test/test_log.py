import pytest
from tortoise import Tortoise
import config.dbsettings as settings
from db.models import Log


class TortoiseTestContext:
    """ 上下文管理器用于初始化和关闭 Tortoise ORM """

    async def __aenter__(self):
        # 初始化 Tortoise ORM
        await Tortoise.init(config=settings.TORTOISE_ORM_POSTGRESQL_DEV)
        # 生成数据库模式（如果尚未生成）
        # await Tortoise.generate_schemas()

    async def __aexit__(self, exc_type, exc, tb):
        # 关闭数据库连接
        await Tortoise.close_connections()





async def add_log():
    await Log.create(message="数据库初始化111", level="INFO", source="AiHelper")


async def query_logs():
    # 查询所有学生记录
    log = await Log.all()
    # 遍历并打印每个学生的详细信息
    from pytz import timezone
    import pytz

    local_tz = timezone('Asia/Shanghai')  # 例如 ''
    log = await Log.all()

    for item in log:
        print(f"\r\n ID: {item.id}, message: {item.message},"
              f" created_at_未处理: {item.created_at},"
              f"created_at_replace: {item.created_at.replace(tzinfo=pytz.utc).astimezone(local_tz)},"
              f" created_at_只读属性: {item.created_at_local},"
              f" updated_at_自定义类型: {item.updated_at.get_beijing_time()}",
              f" updated_at2_自定义类型: {item.updated_at.get_beijing_time()}")
    return log


# 删除记录
# @pytest.fixture(scope="session")
async def clear_logs():
    await Log.all().delete()


@pytest.mark.asyncio
async def test_query_log():
    async with TortoiseTestContext():
        await clear_logs()
        await add_log()
        logs = await query_logs()
        assert len(logs) > 0
