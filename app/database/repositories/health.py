from sqlalchemy import select
from sqlalchemy.orm import joinedload
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas.health import AddHealthSchema
from app.database.models.health import HealthOrm


class HealthRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def add_one(self, data: AddHealthSchema) -> None:
        health = HealthOrm(**data.model_dump())
        self.session.add(health)
        await self.session.commit()

    async def get_all_health(self) -> HealthOrm:
        query = (
            select(HealthOrm)
            .options(joinedload(HealthOrm.health_title))
            .options(joinedload(HealthOrm.health_state))
        )
        result = await self.session.scalars(query)
        return result
