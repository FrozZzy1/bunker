from random import choice

from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas.baggage import AddBaggageSchema, ReadBaggageSchema
from app.database.repositories.baggage import BaggageRepository


class BaggageService:
    def __init__(self, session: AsyncSession) -> None:
        self.baggage_repository = BaggageRepository(session)

    async def create_baggage(self, baggage: AddBaggageSchema) -> None:
        await self.baggage_repository.add_one(baggage)

    async def get_all_baggages(self) -> list[ReadBaggageSchema]:
        baggages = await self.baggage_repository.get_all()
        return baggages
    
    async def get_random_id(self) -> int:
        baggages_id = await self.baggage_repository.get_all_id()
        return choice(baggages_id)
    