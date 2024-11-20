from sqlalchemy import select

from app.api.schemas.health import ReadHealthSchema
from app.api.schemas.hobby import AddHobbySchema
from app.database.models.hobby import HobbyOrm
from app.utils.repository import AbsRepo


class HobbyRepository(AbsRepo):
    async def add_one(self, data: AddHobbySchema) -> None:
        hobby = HobbyOrm(**data.model_dump())
        self.session.add(hobby)
        await self.session.commit()

    async def get_all(self) -> list[ReadHealthSchema]:
        query = select(HobbyOrm)
        result = await self.session.scalars(query)
        return [ReadHealthSchema.model_validate(i) for i in result]
    
    async def get_all_id(self) -> list[int]:
        query = select(HobbyOrm.id)
        result = await self.session.scalars(query)
        return list(result)
