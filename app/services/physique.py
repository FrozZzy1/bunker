from random import choice
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas.physique import AddPhysiqueSchema, ReadPhysiqueSchema
from app.api.schemas.response import ResponseSchema
from app.database.repositories.physique import PhysiqueRepository


class PhysiqueService:
    def __init__(self, session: AsyncSession) -> None:
        self.physique_repo = PhysiqueRepository(session)

    async def create_physique(self, physique: AddPhysiqueSchema) -> ResponseSchema:
        physique = await self.physique_repo.add_one(physique)
        return ResponseSchema(
            data={'physique': physique.model_dump()},
            messages=[f'Physique with id={physique.id} added successfully'],
        )

    async def get_all_physique(self) -> ResponseSchema:
        physique = await self.physique_repo.get_all()
        data = [i.model_dump() for i in physique]
        return ResponseSchema(
            data={'physique': data},
            messages=['All physique retrieved successfully'],
        )
    
    async def get_random_id(self) -> int:
        physiques_id = await self.physique_repo.get_all_id()
        return choice(physiques_id)
