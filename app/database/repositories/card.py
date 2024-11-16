from sqlalchemy import select
from sqlalchemy.orm import joinedload

from app.api.schemas.card import AddCardSchema
from app.utils.repository import AbsRepo
from app.database.models.card import CardOrm
from app.database.models.health import HealthOrm
from app.database.models.baggage import BaggageOrm


class CardRepository(AbsRepo):
    async def add_one(self, data: AddCardSchema) -> None:
        card = CardOrm(**data.model_dump())
        self.session.add(card)
        await self.session.commit()

    async def get_all(self) -> list[CardOrm]:
        query = (
            select(CardOrm)
            .options(joinedload(CardOrm.profession))
            .options(joinedload(CardOrm.phobia))
            .options(joinedload(CardOrm.health)
                .options(joinedload(HealthOrm.health_title))
                .options(joinedload(HealthOrm.health_state)))
            .options(joinedload(CardOrm.baggage))
            .options(joinedload(CardOrm.trait))
            .options(joinedload(CardOrm.physique))
            .options(joinedload(CardOrm.genderage))
            .options(joinedload(CardOrm.hobby))
        )
        return await self.session.scalars(query)
