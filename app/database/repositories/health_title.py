from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas.health import AddHealthTitleSchema
from app.database.models.health import HealthTitleOrm


class HealthTitleRepository(AbsRepo):
    async def add_one(self, data: AddHealthTitleSchema) -> None:
        health = HealthTitleOrm(**data.model_dump())
        self.session.add(health)
        await self.session.commit()

    async def get_all_health_titles(self) -> HealthTitleOrm:
        query = select(HealthTitleOrm)
        result = await self.session.scalars(query)
        return result
