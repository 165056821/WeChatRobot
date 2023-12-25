from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "log2" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "message" TEXT NOT NULL,
    "level" VARCHAR(10) NOT NULL,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "source" VARCHAR(50),
    "extra_info" JSONB
);
COMMENT ON COLUMN "log2"."id" IS '主键';
COMMENT ON COLUMN "log2"."message" IS '日志信息';
COMMENT ON COLUMN "log2"."level" IS '日志级别';
COMMENT ON COLUMN "log2"."created_at" IS '创建时间';
COMMENT ON COLUMN "log2"."updated_at" IS '更新时间';
COMMENT ON COLUMN "log2"."source" IS '日志来源';
COMMENT ON COLUMN "log2"."extra_info" IS '额外信息';
COMMENT ON TABLE "log2" IS '日志表2';"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "log2";"""
