from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas.profession import AddProfessionSchema
from app.database.models.profession import ProfessionOrm
from app.utils.repository import AbsRepo


class ProfessionRepository(AbsRepo):
    async def add_one(self, data: AddProfessionSchema) -> None:
        profession = ProfessionOrm(**data.model_dump())
        self.session.add(profession)
        await self.session.commit()

    async def get_all(self) -> list[ProfessionOrm]:
        query = select(ProfessionOrm)
        result = await self.session.scalars(query)
        return result
