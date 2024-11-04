from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from app.core.config import DATABASE_URL
from app.database.models.base import BaseOrm

async_engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(async_engine, expire_on_commit=False)


async def create_tables():
    async with async_engine.begin() as connect:
        await connect.run_sync(BaseOrm.metadata.create_all)


async def delete_tables():
    async with async_engine.begin() as connect:
        await connect.run_sync(BaseOrm.metadata.drop_all)
