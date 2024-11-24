from random import choice
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas.hobby import AddHobbySchema, ReadHobbySchema
from app.api.schemas.response import ResponseSchema
from app.database.repositories.hobby import HobbyRepository


class HobbyService:
    def __init__(self, session: AsyncSession) -> None:
        self.hobby_repo = HobbyRepository(session)

    async def create_hobby(self, hobby: AddHobbySchema) -> ResponseSchema:
        hobby = await self.hobby_repo.add_one(hobby)
        return ResponseSchema(
            data=hobby.model_dump(),
            messages=[f'Hobby with id={hobby.id} added successfully'],
        )

    async def get_all_hobbies(self) -> list[ReadHobbySchema]:
        hobbies = await self.hobby_repo.get_all()
        return hobbies
    
    async def get_random_id(self) -> int:
        hobbies_id = await self.hobby_repo.get_all_id()
        return choice(hobbies_id)
