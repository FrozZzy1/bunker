from sqlalchemy import select

from app.api.schemas.genderage import AddGenderageSchema
from app.database.models.genderage import GenderageOrm
from app.utils.repository import AbsRepo


class GenderageRepository(AbsRepo):
    async def add_one(self, data: AddGenderageSchema) -> None:
        genderage = GenderageOrm(**data.model_dump())
        self.session.add(genderage)
        await self.session.commit()

    async def get_all_genderages(self) -> list[GenderageOrm]:
        query = select(GenderageOrm)
        return await self.session.scalars(query)
