from sqlalchemy import select
from sqlalchemy.orm import joinedload
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.models.card import CardOrm


class CardRepository:
    @classmethod
    async def add_one(cls, session: AsyncSession, data: dict) -> None:
        card = CardOrm(**data.model_dump())
        session.add(card)
        await session.commit()
        await session.refresh(card)

    @classmethod
    async def get_all(cls, session: AsyncSession) -> list[CardOrm]:
        query = (
            select(CardOrm)
            .options(
                joinedload(CardOrm.profession)
            )
        )
        result = await session.scalars(query)
        return result
