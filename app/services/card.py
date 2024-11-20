from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas.card import AddCardSchema, ReadCardSchema
from app.database.repositories.card import CardRepository


class CardService:
    def __init__(self, session: AsyncSession) -> None:
        self.card_repository = CardRepository(session)

    async def create_card(self) -> None:
        card = AddCardSchema()
        await self.card_repository.add_one(card)

    async def get_all_cards(self) -> list[ReadCardSchema]:
        cards = await self.card_repository.get_all()
        return cards
