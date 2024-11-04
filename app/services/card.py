from app.api.schemas.card import AddCardSchema
from app.database.models.card import CardOrm
from app.database.repositories.card import CardRepository


class CardService:
    @classmethod
    async def create_card(cls, card: AddCardSchema) -> None:
        card_dict = card.model_dump()
        await CardRepository.add_one(card_dict)

    @classmethod
    async def get_all_cards(cls) -> list[CardOrm]:
        cards = await CardRepository.get_all()
        return cards
