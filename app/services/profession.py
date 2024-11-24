from random import choice
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas.profession import AddProfessionSchema, ReadProfessionSchema
from app.api.schemas.response import ResponseSchema
from app.database.repositories.profession import ProfessionRepository


class ProfessionService:
    def __init__(self, session: AsyncSession) -> None:
        self.profession_repository = ProfessionRepository(session)

    async def create_profession(self, profession: AddProfessionSchema) -> ResponseSchema:
        profession = await self.profession_repository.add_one(profession)
        return ResponseSchema(
            data=profession.model_dump(),
            messages=[f'Profession with id={profession.id} added successfully'],
        )

    async def get_all_professions(self) -> ResponseSchema:
        professions = await self.profession_repository.get_all()
        data = [i.model_dump() for i in professions]
        return ResponseSchema(
            data={'professions': data},
            messages=['All professions retrieved successfully'],
        )
    
    async def get_random_id(self) -> int:
        professions_id = await self.profession_repository.get_all_id()
        return choice(professions_id)
