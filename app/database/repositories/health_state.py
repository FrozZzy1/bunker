from sqlalchemy import select

from app.api.schemas.health import AddHealthStateSchema, ReadHealthStateSchema
from app.database.models.health import HealthStateOrm
from app.utils.repository import AbsRepo



class HealthStateRepository(AbsRepo):
    async def add_one(self, data: AddHealthStateSchema) -> ReadHealthStateSchema:
        health = HealthStateOrm(**data.model_dump())
        self.session.add(health)
        await self.session.commit()
        await self.session.refresh(health)
        return ReadHealthStateSchema.model_validate(health)

    async def get_all(self) -> list[ReadHealthStateSchema]:
        query = select(HealthStateOrm)
        result = await self.session.scalars(query)
        return [ReadHealthStateSchema.model_validate(i) for i in result]
    
    async def get_all_id(self) -> list[int]:
        query = select(HealthStateOrm.id)
        result = await self.session.scalars(query)
        return list(result)
