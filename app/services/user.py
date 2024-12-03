from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError

from app.api.schemas.response import ResponseSchema
from app.api.schemas.user import AddUserSchema, ReadUserSchema, UpdateUserSchema
from app.database.repositories.user import UserRepository
from app.utils.logging import setup_logger

logger = setup_logger()


class UserService:
    def __init__(self, session: AsyncSession) -> None:
        self.user_repository = UserRepository(session)

    async def create_user(self, user: AddUserSchema) -> ResponseSchema:
        try:
            user = await self.user_repository.add_one(user)
        except IntegrityError:
            return ResponseSchema(
                data=user.model_dump(),
                errors={'tg_id': [f'User with tg_id={user.tg_id} already exists']},
            )
        return ResponseSchema(
            data=user.model_dump(),
            messages=[f'User with id={user.id} added successfully'],
        )

    async def get_all_users(self) -> ResponseSchema:
        users = await self.user_repository.get_all()
        data = [i.model_dump() for i in users]
        return ResponseSchema(
            data={'users': data},
            messages=['All users retrieved successfully'],
        )
    
    async def update_user(self, tg_id: int, user: UpdateUserSchema) -> ResponseSchema:
        user = await self.user_repository.update(tg_id, user)
        return ResponseSchema(
            data={'user': user.model_dump()},
            messages=['Имя игрока успешно обновлено.'],
        )
