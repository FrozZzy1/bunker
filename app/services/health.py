from random import choice
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas.health import AddHealthSchema, ReadHealthSchema
from app.api.schemas.response import ResponseSchema
from app.database.repositories.health import HealthRepository
from app.services.health_state import HealthStateService
from app.services.health_title import HealthTitleService


class HealthService:
    def __init__(self, session: AsyncSession) -> None:
        self.health_repository = HealthRepository(session)
        self.health_title_service = HealthTitleService(session)
        self.health_state_service = HealthStateService(session)

    async def create_health(self) -> ResponseSchema:
        health = AddHealthSchema(
            health_title_id=await self.health_title_service.get_random_id(),
            health_state_id=await self.health_title_service.get_random_id(),
        )
        health = await self.health_repository.add_one(health)
        return ResponseSchema(
            data=health.model_dump(),
            messages=[f'Health with id={health.id} added successfully'],
        )

    async def get_all_health(self) -> list[ReadHealthSchema]:
        health = await self.health_repository.get_all()
        return health
    
    async def get_random_id(self) -> int:
        health_id = await self.health_repository.get_all_id()
        return choice(health_id)
