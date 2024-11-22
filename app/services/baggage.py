from random import choice

from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas.baggage import AddBaggageSchema, ReadBaggageSchema
from app.api.schemas.response import ResponseSchema
from app.database.repositories.baggage import BaggageRepository


class BaggageService:
    def __init__(self, session: AsyncSession) -> None:
        self.baggage_repository = BaggageRepository(session)

    async def create_baggage(self, baggage: AddBaggageSchema) -> dict:
        baggage = await self.baggage_repository.add_one(baggage)
        
        return ResponseSchema(
            data=baggage.model_dump(),
            messages=[f'Baggage with id={baggage.id} added successfully']
        )

    async def get_all_baggages(self) -> list[ReadBaggageSchema]:
        baggages = await self.baggage_repository.get_all()
        return baggages
    
    async def get_random_id(self) -> int:
        baggages_id = await self.baggage_repository.get_all_id()
        return choice(baggages_id)
    