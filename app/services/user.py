from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError

from app.api.schemas.user import AddUserSchema
from app.database.models.user import UserOrm
from app.database.repositories.user import UserRepository
from app.utils.logging import setup_logger

logger = setup_logger()


class UserService:
    @classmethod
    async def create_user(cls, session: AsyncSession, user: AddUserSchema) -> None:
        try:
            await UserRepository.add_one(session, user)
        except IntegrityError:
            logger.error(f'User with tg_id={user.tg_id} already exists')
            # TODO: вынести rollback отдельно
            await session.rollback()

    @classmethod
    async def get_all_users(cls, session: AsyncSession) -> list[UserOrm]:
        users = await UserRepository.get_all(session)
        return users
