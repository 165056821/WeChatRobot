from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "log" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "message" TEXT NOT NULL,
    "level" VARCHAR(10) NOT NULL,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "source" VARCHAR(50),
    "extra_info" JSONB
);
COMMENT ON COLUMN "log"."id" IS '主键';
COMMENT ON COLUMN "log"."message" IS '日志信息';
COMMENT ON COLUMN "log"."level" IS '日志级别';
COMMENT ON COLUMN "log"."created_at" IS '创建时间';
COMMENT ON COLUMN "log"."updated_at" IS '更新时间';
COMMENT ON COLUMN "log"."source" IS '日志来源';
COMMENT ON COLUMN "log"."extra_info" IS '额外信息';
COMMENT ON TABLE "log" IS '日志表';
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
