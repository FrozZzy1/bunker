from sqlalchemy import select, update
from sqlalchemy.exc import IntegrityError

from app.api.schemas.user import AddUserSchema, ReadUserSchema, UpdateUserSchema
from app.database.models.user import UserOrm
from app.utils.logging import setup_logger
from app.utils.repository import AbsRepo
from app.utils.repository import AbsRepo

logger = setup_logger()


class UserRepository(AbsRepo):
    async def add_one(self, data: AddUserSchema) -> ReadUserSchema:
        user = UserOrm(**data.model_dump())
        try:
            self.session.add(user)
            await self.session.commit()
        except IntegrityError:
            await self.session.rollback()
            raise
        await self.session.refresh(user)
        return ReadUserSchema.model_validate(user)

    async def get_all(self) -> list[ReadUserSchema]:
        query = select(UserOrm)
        result = await self.session.scalars(query)
        return [ReadUserSchema.model_validate(i) for i in result]

    async def update(self, id: int, user: UpdateUserSchema) -> ReadUserSchema:
        query = (
            update(UserOrm)
            .filter(UserOrm.id == id)
            .values(name=user.name)
        )
        await self.session.execute(query)
        query = select(UserOrm).filter(UserOrm.id == id)
        result = await self.session.scalars(query)
        return ReadUserSchema.model_validate(result)
