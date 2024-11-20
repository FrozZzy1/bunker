from random import choice
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas.genderage import AddGenderageSchema, ReadGenderageSchema
from app.database.repositories.genderage import GenderageRepository


class GenderageService:
    def __init__(self, session: AsyncSession) -> None:
        self.genderage_repo = GenderageRepository(session)

    async def create_genderage(self, genderage: AddGenderageSchema) -> None:
        await self.genderage_repo.add_one(genderage)

    async def get_all_genderages(self) -> list[ReadGenderageSchema]:
        genderages = await self.genderage_repo.get_all_genderages()
        return genderages
    
    async def get_random_id(self) -> int:
        genderages_id = await self.genderage_repo.get_all_id()
        return choice(genderages_id)
