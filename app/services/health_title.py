from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas.health import AddHealthTitleSchema
from app.database.models.health import HealthTitleOrm
from app.database.repositories.health_title import HealthTitleRepository


class HealthTitleService:
    def __init__(self, session: AsyncSession) -> None:
        self.health_title_repository = HealthTitleRepository(session)

    async def create_health_title(self, health_title: AddHealthTitleSchema) -> None:
        await self.health_title_repository.add_one(health_title)

    async def get_all_health_titles(self) -> list[HealthTitleOrm]:
        health_titles = await self.health_title_repository.get_all_health_titles()
        return health_titles
