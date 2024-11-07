from sqlalchemy import select
from sqlalchemy.orm import joinedload
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas.card import AddCardSchema
from app.database.models.card import CardOrm


class CardRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def add_one(self, data: AddCardSchema) -> None:
        card = CardOrm(**data.model_dump())
        self.session.add(card)
        await self.session.commit()
        await self.session.refresh(card)

    async def get_all(self) -> list[CardOrm]:
        query = (
            select(CardOrm)
            .options(joinedload(CardOrm.profession))
        )
        result = await self.session.scalars(query)
        return result
