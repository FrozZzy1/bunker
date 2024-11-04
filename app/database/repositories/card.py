from sqlalchemy import select
from sqlalchemy.orm import joinedload

from app.database.database import async_session_maker
from app.database.models.card import CardOrm


class CardRepository:
    @staticmethod
    async def add_one(data: dict) -> None:
        async with async_session_maker() as session:
            card = CardOrm(**data)
            session.add(card)
            await session.commit()
            await session.refresh(card)

    @staticmethod
    async def get_all() -> list[CardOrm]:
        async with async_session_maker() as session:
            query = (
                select(CardOrm)
                .options(
                    joinedload(CardOrm.profession)
                )
            )
            result = await session.scalars(query)
            return result
