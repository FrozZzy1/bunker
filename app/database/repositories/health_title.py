from sqlalchemy import select

from app.api.schemas.health import AddHealthTitleSchema, ReadHealthTitleSchema
from app.database.models.health import HealthTitleOrm
from app.utils.repository import AbsRepo


class HealthTitleRepository(AbsRepo):
    async def add_one(self, data: AddHealthTitleSchema) -> ReadHealthTitleSchema:
        health = HealthTitleOrm(**data.model_dump())
        self.session.add(health)
        await self.session.commit()
        await self.session.refresh(health)
        return ReadHealthTitleSchema.model_validate(health)

    async def get_all(self) -> list[ReadHealthTitleSchema]:
        query = select(HealthTitleOrm)
        result = await self.session.scalars(query)
        return [ReadHealthTitleSchema.model_validate(i) for i in result]
    
    async def get_all_id(self) -> list[int]:
        query = select(HealthTitleOrm.id)
        result = await self.session.scalars(query)
        return list(result)
