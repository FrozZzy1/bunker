from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas.phobia import AddPhobiaSchema
from app.database.models.phobia import PhobiaOrm
from app.database.repositories.phobia import PhobiaRepository


class PhobiaService:
    def __init__(self, session: AsyncSession) -> None:
        self.phobia_repository = PhobiaRepository(session)

    async def create_phobia(self, phobia: AddPhobiaSchema) -> None:
        await self.phobia_repository.add_one(phobia)

    async def get_all_phobias(self) -> list[PhobiaOrm]:
        phobias = await self.phobia_repository.get_all_phobias()
        return phobias
