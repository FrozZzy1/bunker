from sqlalchemy import select

from app.database.database import async_session_maker
from app.database.models.user import UserOrm


class UserRepository:
    @staticmethod
    async def add_one(data: dict) -> None:
        async with async_session_maker() as session:
            user = UserOrm(**data)
            session.add(user)
            await session.commit()
            await session.refresh(user)

    @staticmethod
    async def get_all() -> list[UserOrm]:
        async with async_session_maker() as session:
            query = select(UserOrm)
            result = await session.scalars(query)
            return result
