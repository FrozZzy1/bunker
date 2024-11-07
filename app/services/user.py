from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError

from app.api.schemas.user import AddUserSchema
from app.database.models.user import UserOrm
from app.database.repositories.user import UserRepository
from app.utils.logging import setup_logger

logger = setup_logger()


class UserService:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session
        self.user_repository = UserRepository(session)

    async def create_user(self, user: AddUserSchema) -> None:
        try:
            await self.user_repository.add_one(user)
        except IntegrityError:
            logger.error(f'User with tg_id={user.tg_id} already exists')
            # TODO: вынести rollback отдельно
            await self.session.rollback()

    async def get_all_users(self) -> list[UserOrm]:
        users = await self.user_repository.get_all()
        return users
