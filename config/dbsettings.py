
TORTOISE_ORM_POSTGRESQL_DEV = {
    'connections': {
        # 这里的 'default' 是连接名，你可以根据需要定义多个连接
        'default': {
            'engine': 'tortoise.backends.asyncpg',  # 指定 asyncpg 作为后端
            'credentials': {
                'host': '124.221.236.106',  # 数据库服务器地址
                'port': '15432',  # PostgreSQL 端口，默认为 5432
                'user': 'postgres',  # 替换为你的用户名
                'password': '20231219Test',  # 替换为你的密码
                'database': 'aihelper_fastapi_dev',  # 替换为你的数据库名
            }
        },
    },
    'apps': {
        'models': {
            'models': ['db.models', 'aerich.models'],
            'default_connection': 'default',
        },
    },
}


TORTOISE_ORM_POSTGRESQL_TEST = {
    'connections': {
        # 这里的 'default' 是连接名，你可以根据需要定义多个连接
        'default': {
            'engine': 'tortoise.backends.asyncpg',  # 指定 asyncpg 作为后端
            'credentials': {
                'host': '124.221.236.106',  # 数据库服务器地址
                'port': '15432',  # PostgreSQL 端口，默认为 5432
                'user': 'postgres',  # 替换为你的用户名
                'password': '20231219Test',  # 替换为你的密码
                'database': 'aihelper_fastapi_test',  # 替换为你的数据库名
            }
        },
    },
    'apps': {
        'models': {
            'models': ['db.models', 'aerich.models'],
            'default_connection': 'default',
        },
    },
}
TORTOISE_ORM_POSTGRESQL_PROD = {
    'connections': {
        # 这里的 'default' 是连接名，你可以根据需要定义多个连接
        'default': {
            'engine': 'tortoise.backends.asyncpg',  # 指定 asyncpg 作为后端
            'credentials': {
                'host': '124.221.236.106',  # 数据库服务器地址
                'port': '15432',  # PostgreSQL 端口，默认为 5432
                'user': 'postgres',  # 替换为你的用户名
                'password': '20231219Test',  # 替换为你的密码
                'database': 'aihelper_fastapi_prod',  # 替换为你的数据库名
            }
        },
    },
    'apps': {
        'models': {
            'models': ['db.models', 'aerich.models'],
            'default_connection': 'default',
        },
    },
}
