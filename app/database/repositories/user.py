from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from app.api.schemas.user import AddUserSchema, ReadUserSchema
from app.database.models.user import UserOrm
from app.utils.logging import setup_logger
from app.utils.repository import AbsRepo
from app.utils.repository import AbsRepo

logger = setup_logger()


class UserRepository(AbsRepo):
    async def add_one(self, data: AddUserSchema) -> None:
        user = UserOrm(**data.model_dump())
        try:
            self.session.add(user)
            await self.session.commit()
        except IntegrityError:
            await self.session.rollback()
            raise

    async def get_all(self) -> list[ReadUserSchema]:
        query = select(UserOrm)
        result = await self.session.scalars(query)
        return [ReadUserSchema.model_validate(i) for i in result]
