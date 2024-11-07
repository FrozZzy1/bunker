from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas.user import AddUserSchema
from app.database.models.user import UserOrm
from app.utils.logging import setup_logger

logger = setup_logger()


class UserRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def add_one(self, data: AddUserSchema) -> None:
        user = UserOrm(**data.model_dump())
        self.session.add(user)
        await self.session.commit()
        await self.session.refresh(user)

    async def get_all(self) -> list[UserOrm]:
        query = select(UserOrm)
        result = await self.session.scalars(query)
        return result
