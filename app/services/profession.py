from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas.profession import AddProfessionSchema
from app.database.models.profession import ProfessionOrm
from app.database.repositories.profession import ProfessionRepository


class ProfessionService:
    @classmethod
    async def create_profession(cls, session: AsyncSession, profession: AddProfessionSchema) -> None:
        await ProfessionRepository.add_one(session, profession)

    @classmethod
    async def get_all_professions(cls, session: AsyncSession) -> list[ProfessionOrm]:
        professions = await ProfessionRepository.get_all(session)
        return professions
