from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas.physique import AddPhysiqueSchema
from app.database.models.physique import PhysiqueOrm
from app.database.repositories.physique import PhysiqueRepository


class PhysiqueService:
    def __init__(self, session: AsyncSession) -> None:
        self.physique_repo = PhysiqueRepository(session)

    async def create_physique(self, physique: AddPhysiqueSchema) -> None:
        await self.physique_repo.add_one(physique)

    async def get_all_physique(self) -> list[PhysiqueOrm]:
        physique = await self.physique_repo.get_all_physique()
        return physique
