from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas.user import AddUserSchema
from app.database.models.user import UserOrm
from app.utils.logging import setup_logger

logger = setup_logger()


class UserRepository:
    @classmethod
    async def add_one(cls, session: AsyncSession, data: AddUserSchema) -> None:
        user = UserOrm(**data.model_dump())
        session.add(user)
        await session.commit()
        await session.refresh(user)

    @classmethod
    async def get_all(cls, session: AsyncSession) -> list[UserOrm]:
        query = select(UserOrm)
        result = await session.scalars(query)
        return result
