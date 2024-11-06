from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas.card import AddCardSchema
from app.database.models.card import CardOrm
from app.database.repositories.card import CardRepository


class CardService:
    @classmethod
    async def create_card(cls, session: AsyncSession, card: AddCardSchema) -> None:
        await CardRepository.add_one(session, card)

    @classmethod
    async def get_all_cards(cls, session: AsyncSession) -> list[CardOrm]:
        cards = await CardRepository.get_all(session)
        return cards
