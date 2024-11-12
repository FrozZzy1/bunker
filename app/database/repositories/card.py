from sqlalchemy import select
from sqlalchemy.orm import joinedload
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas.card import AddCardSchema
from app.database.models.card import CardOrm
from app.database.models.health import HealthOrm


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
                .options(joinedload(HealthOrm.health_state))
            )
        )
        result = await self.session.scalars(query)
        return result
