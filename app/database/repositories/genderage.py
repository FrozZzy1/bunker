from sqlalchemy import select

from app.api.schemas.genderage import AddGenderageSchema, ReadGenderageSchema
from app.database.models.genderage import GenderageOrm
from app.utils.repository import AbsRepo


class GenderageRepository(AbsRepo):
    async def add_one(self, data: AddGenderageSchema) -> ReadGenderageSchema:
        genderage = GenderageOrm(**data.model_dump())
        self.session.add(genderage)
        await self.session.commit()
        await self.session.refresh(genderage)
        return ReadGenderageSchema.model_validate(genderage)

    async def get_all(self) -> list[ReadGenderageSchema]:
        query = select(GenderageOrm)
        result = await self.session.scalars(query)
        return [ReadGenderageSchema.model_validate(i) for i in result]

    async def get_all_id(self) -> list[int]:
        query = select(GenderageOrm.id)
        result = await self.session.scalars(query)
        return list(result)

