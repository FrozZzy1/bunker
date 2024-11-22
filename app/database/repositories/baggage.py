from sqlalchemy import select

from app.api.schemas.baggage import AddBaggageSchema, ReadBaggageSchema
from app.database.models.baggage import BaggageOrm
from app.utils.repository import AbsRepo


class BaggageRepository(AbsRepo):
    async def add_one(self, data: AddBaggageSchema) -> ReadBaggageSchema:
        baggage = BaggageOrm(**data.model_dump())
        self.session.add(baggage)
        await self.session.commit()
        await self.session.refresh(baggage)
        return ReadBaggageSchema.model_validate(baggage)


    async def get_all(self) -> list[ReadBaggageSchema]:
        query = select(BaggageOrm)
        result = await self.session.scalars(query)
        return [ReadBaggageSchema.model_validate(i) for i in result]

    async def get_all_id(self) -> list[int]:
        query = select(BaggageOrm.id)
        result = await self.session.scalars(query)
        return list(result)

