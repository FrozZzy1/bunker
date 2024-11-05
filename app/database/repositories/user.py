from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from app.database.database import async_session_maker
from app.database.models.user import UserOrm
from app.utils.logging import setup_logger

logger = setup_logger()


class UserRepository:
    @staticmethod
    async def add_one(data: dict) -> None:
        async with async_session_maker() as session:
            user = UserOrm(**data)
            try:
                session.add(user)
                await session.commit()
            except IntegrityError:
                await session.rollback()
                # TODO: сепарировать строчку
                logger.exception(f'User with tg_id={data["tg_id"]} already exists')
            else:
                await session.refresh(user)

    @staticmethod
    async def get_all() -> list[UserOrm]:
        async with async_session_maker() as session:
            query = select(UserOrm)
            result = await session.scalars(query)
            return result
