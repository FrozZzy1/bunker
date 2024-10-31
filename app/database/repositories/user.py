from sqlalchemy import select

from app.database.database import async_session_maker
from app.database.models.user import UserOrm


class UserRepository:
    @classmethod
    async def add_user(cls, data: dict) -> UserOrm:
        async with async_session_maker() as session:
            user = UserOrm(**data)
            session.add(user)
            await session.commit()
            await session.refresh(user)

            return user

    @classmethod
    async def get_users(cls) -> list[UserOrm]:
        async with async_session_maker() as session:
            query = select(UserOrm)
            result = await session.scalars(query)

            return result
