from sqlalchemy import select

from app.api.schemas.card import AddCardSchema, ReadCardSchema
from app.utils.repository import AbsRepo
from app.database.models.card import CardOrm


class CardRepository(AbsRepo):
    async def add_one(self, data: AddCardSchema) -> ReadCardSchema:
        card = CardOrm(**data.model_dump())
        self.session.add(card)
        await self.session.commit()
        await self.session.refresh(card)
        return ReadCardSchema.model_validate(card)

    async def get_all(self) -> list[ReadCardSchema]:
        query = select(CardOrm)
        result = await self.session.scalars(query)
        return [ReadCardSchema.model_validate(i) for i in result]
