from sqlalchemy import select

from app.api.schemas.baggage import AddBaggageSchema
from app.database.models.baggage import BaggageOrm
from app.utils.repository import AbsRepo


class BaggageRepository(AbsRepo):
    async def add_one(self, data: AddBaggageSchema) -> None:
        baggage = BaggageOrm(**data.model_dump())
        self.session.add(baggage)
        await self.session.commit()

    async def get_all(self) -> list[BaggageOrm]:
        query = select(BaggageOrm)
        result = await self.session.scalars(query)
        return result
