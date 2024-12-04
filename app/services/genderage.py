from random import choice
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas.genderage import AddGenderageSchema
from app.api.schemas.response import ResponseSchema
from app.database.repositories.genderage import GenderageRepository


class GenderageService:
    def __init__(self, session: AsyncSession) -> None:
        self.genderage_repo = GenderageRepository(session)

    async def create_genderage(self, genderage: AddGenderageSchema) -> ResponseSchema:
        genderage = await self.genderage_repo.add_one(genderage)
        return ResponseSchema(
            data={'genderage': genderage.model_dump()},
            messages=[f'Genderage with id={genderage.id} added successfully'],
        )

    async def get_all_genderages(self) -> ResponseSchema:
        genderages = await self.genderage_repo.get_all()
        data = [i.model_dump() for i in genderages]
        return ResponseSchema(
            data={'genderages': data},
            messages=['All genderages retrieved successfully'],
        )
    
    async def get_random_id(self) -> int:
        genderages_id = await self.genderage_repo.get_all_id()
        return choice(genderages_id)
