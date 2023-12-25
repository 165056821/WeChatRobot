from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "log" ADD "updated_at2" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP;
        ALTER TABLE "log" ALTER COLUMN "updated_at" TYPE TIMESTAMPTZ USING "updated_at"::TIMESTAMPTZ;
        DROP TABLE IF EXISTS "log2";"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "log" DROP COLUMN "updated_at2";
        ALTER TABLE "log" ALTER COLUMN "updated_at" TYPE TIMESTAMPTZ USING "updated_at"::TIMESTAMPTZ;"""
