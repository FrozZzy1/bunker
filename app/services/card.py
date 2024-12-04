from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas.card import AddCardSchema
from app.database.repositories.card import CardRepository
from app.services.baggage import BaggageService
from app.services.genderage import GenderageService
from app.services.health import HealthService
from app.services.hobby import HobbyService
from app.services.phobia import PhobiaService
from app.services.physique import PhysiqueService
from app.services.profession import ProfessionService
from app.services.trait import TraitService
from app.api.schemas.response import ResponseSchema


class CardService:
    def __init__(self, session: AsyncSession) -> None:
        self.card_repository = CardRepository(session)
        self.baggage_service = BaggageService(session)
        self.genderage_service = GenderageService(session)
        self.health_service = HealthService(session)
        self.hobby_service = HobbyService(session)
        self.phobia_service = PhobiaService(session)
        self.physique_service = PhysiqueService(session)
        self.profession_service = ProfessionService(session)
        self.trait_service = TraitService(session)


    async def create_card(self) -> ResponseSchema:
        card = AddCardSchema(
            health_id=await self.health_service.get_random_id(),
            profession_id=await self.profession_service.get_random_id(),
            phobia_id=await self.phobia_service.get_random_id(),
            baggage_id=await self.baggage_service.get_random_id(),
            hobby_id=await self.hobby_service.get_random_id(),
            trait_id=await self.trait_service.get_random_id(),
            physique_id=await self.physique_service.get_random_id(),
            genderage_id=await self.genderage_service.get_random_id(),
        )
        card = await self.card_repository.add_one(card)
        return ResponseSchema(
            data={'card': card.model_dump()},
            messages=[f'Card with id={card.id} added successfully'],
        )


    async def get_all_cards(self) -> ResponseSchema:
        cards = await self.card_repository.get_all()
        data = [i.model_dump() for i in cards]
        return ResponseSchema(
            data={'cards': data},
            messages=['All cards retrieved successfully'],
        )
