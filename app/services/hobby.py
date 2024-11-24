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

    async def get_all_hobbies(self) -> ResponseSchema:
        hobbies = await self.hobby_repo.get_all()
        data = [i.model_dump() for i in hobbies]
        return ResponseSchema(
            data={'hobbies': data},
            message=['All hobbies retrieved successfully'],
        )
    
    async def get_random_id(self) -> int:
        hobbies_id = await self.hobby_repo.get_all_id()
        return choice(hobbies_id)
