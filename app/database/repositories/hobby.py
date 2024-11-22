from sqlalchemy import select

from app.api.schemas.hobby import AddHobbySchema, ReadHobbySchema
from app.database.models.hobby import HobbyOrm
from app.utils.repository import AbsRepo


class HobbyRepository(AbsRepo):
    async def add_one(self, data: AddHobbySchema) -> ReadHobbySchema:
        hobby = HobbyOrm(**data.model_dump())
        self.session.add(hobby)
        await self.session.commit()
        await self.session.refresh(hobby)
        return ReadHobbySchema.model_validate(hobby)

    async def get_all(self) -> list[ReadHobbySchema]:
        query = select(HobbyOrm)
        result = await self.session.scalars(query)
        return [ReadHobbySchema.model_validate(i) for i in result]
    
    async def get_all_id(self) -> list[int]:
        query = select(HobbyOrm.id)
        result = await self.session.scalars(query)
        return list(result)
