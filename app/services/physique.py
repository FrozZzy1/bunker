from random import choice
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas.physique import AddPhysiqueSchema, ReadPhysiqueSchema
from app.database.repositories.physique import PhysiqueRepository


class PhysiqueService:
    def __init__(self, session: AsyncSession) -> None:
        self.physique_repo = PhysiqueRepository(session)

    async def create_physique(self, physique: AddPhysiqueSchema) -> None:
        await self.physique_repo.add_one(physique)

    async def get_all_physique(self) -> list[ReadPhysiqueSchema]:
        physique = await self.physique_repo.get_all_physique()
        return physique
    
    async def get_random_id(self) -> int:
        physiques_id = await self.physique_repo.get_all_id()
        return choice(physiques_id)
