from sqlalchemy import select

from app.api.schemas.health import AddHealthSchema, ReadHealthSchema
from app.database.models.health import HealthOrm
from app.utils.repository import AbsRepo


class HealthRepository(AbsRepo):
    async def add_one(self, data: AddHealthSchema) -> ReadHealthSchema:
        health = HealthOrm(**data.model_dump())
        self.session.add(health)
        await self.session.commit()
        await self.session.refresh(health)
        return ReadHealthSchema.model_validate(health)

    async def get_all(self) -> list[ReadHealthSchema]:
        query = select(HealthOrm)
        result = await self.session.scalars(query)
        return [ReadHealthSchema.model_validate(i) for i in result]
    
    async def get_all_id(self) -> list[int]:
        query = select(HealthOrm.id)
        result = await self.session.scalars(query)
        return list(result)
