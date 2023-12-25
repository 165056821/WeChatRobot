# import datetime
# import pytz
# from tortoise import Tortoise, signals
# from config.dbsettings import TORTOISE_ORM_POSTGRESQL_DEV as config
# from db.models import Log
#
# # 定义事件监听器
# async def set_timezone(sender, connection):
#     if connection.schema_generator.DIALECT == "postgres":
#         await connection.execute_script("SET TIME ZONE 'Asia/Shanghai'")
#
# # 初始化数据库函数
# async def init_db():
#     # 注册事件监听器
#     signals.post_init.connect(set_timezone, Tortoise)
#
#     # 初始化数据库
#     await Tortoise.init(config=config)
#
#     # 自动生成数据库模式（如果需要）
#     await Tortoise.generate_schemas()


import datetime

import pytz

from config.dbsettings import TORTOISE_ORM_POSTGRESQL_DEV as config
from db.models import Log


async def init_db():
    # 初始化数据库
    from tortoise import Tortoise
    await Tortoise.init(config=config)
    # 自动生成数据库模式（如果需要）
    await Tortoise.generate_schemas()

