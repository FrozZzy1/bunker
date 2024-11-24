from random import choice
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas.health import AddHealthTitleSchema, ReadHealthTitleSchema
from app.api.schemas.response import ResponseSchema
from app.database.repositories.health_title import HealthTitleRepository


class HealthTitleService:
    def __init__(self, session: AsyncSession) -> None:
        self.health_title_repository = HealthTitleRepository(session)

    async def create_health_title(self, health_title: AddHealthTitleSchema) -> ResponseSchema:
        health_title = await self.health_title_repository.add_one(health_title)
        return ResponseSchema(
            data=health_title.model_dump(),
            messages=[f'Health title with id={health_title.id} added successfully'],
        )

    async def get_all_health_titles(self) -> list[ReadHealthTitleSchema]:
        health_titles = await self.health_title_repository.get_all()
        return health_titles
    
    async def get_random_id(self) -> int:
        health_titles_id = await self.health_title_repository.get_all_id()
        return choice(health_titles_id)
