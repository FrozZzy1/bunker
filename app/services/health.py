from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas.health import AddHealthSchema
from app.database.models.health import HealthOrm
from app.database.repositories.health import HealthRepository


class HealthService:
    def __init__(self, session: AsyncSession) -> None:
        self.health_repository = HealthRepository(session)

    async def create_health(self, health: AddHealthSchema) -> None:
        await self.health_repository.add_one(health)

    async def get_all_health(self) -> list[HealthOrm]:
        health = await self.health_repository.get_all_health()
        return health
