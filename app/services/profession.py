from random import choice
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas.profession import AddProfessionSchema, ReadProfessionSchema
from app.database.repositories.profession import ProfessionRepository


class ProfessionService:
    def __init__(self, session: AsyncSession) -> None:
        self.profession_repository = ProfessionRepository(session)

    async def create_profession(self, profession: AddProfessionSchema) -> None:
        await self.profession_repository.add_one(profession)

    async def get_all_professions(self) -> list[ReadProfessionSchema]:
        professions = await self.profession_repository.get_all()
        return professions
    
    async def get_random_id(self) -> int:
        professions_id = await self.profession_repository.get_all_id()
        return choice(professions_id)
