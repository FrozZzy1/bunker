from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas.profession import AddProfessionSchema
from app.database.models.profession import ProfessionOrm
from app.database.repositories.profession import ProfessionRepository


class ProfessionService:
    def __init__(self, session: AsyncSession) -> None:
        self.profession_repository = ProfessionRepository(session)

    async def create_profession(self, profession: AddProfessionSchema) -> None:
        await self.profession_repository.add_one(profession)

    async def get_all_professions(self) -> list[ProfessionOrm]:
        professions = await self.profession_repository.get_all()
        return professions
