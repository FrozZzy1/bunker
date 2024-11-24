from random import choice
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas.phobia import AddPhobiaSchema, ReadPhobiaSchema
from app.api.schemas.response import ResponseSchema
from app.database.repositories.phobia import PhobiaRepository


class PhobiaService:
    def __init__(self, session: AsyncSession) -> None:
        self.phobia_repository = PhobiaRepository(session)

    async def create_phobia(self, phobia: AddPhobiaSchema) -> ResponseSchema:
        phobia = await self.phobia_repository.add_one(phobia)
        return ResponseSchema(
            data=phobia.model_dump(),
            messages=[f'Phobia with id={phobia.id} added successfully'],
        )

    async def get_all_phobias(self) -> list[ReadPhobiaSchema]:
        phobias = await self.phobia_repository.get_all()
        return phobias
    
    async def get_random_id(self) -> int:
        phobias_id = await self.phobia_repository.get_all_id()
        return choice(phobias_id)
