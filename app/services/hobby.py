from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas.hobby import AddHobbySchema
from app.database.models.hobby import HobbyOrm
from app.database.repositories.hobby import HobbyRepository


class HobbyService:
    def __init__(self, session: AsyncSession) -> None:
        self.hobby_repo = HobbyRepository(session)

    async def create_hobby(self, hobby: AddHobbySchema) -> None:
        await self.hobby_repo.add_one(hobby)

    async def get_all_hobbies(self) -> list[HobbyOrm]:
        hobbies = await self.hobby_repo.get_all_hobbies()
        return hobbies
