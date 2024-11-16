from sqlalchemy import select
from sqlalchemy.orm import selectinload, joinedload

from app.api.schemas.player import AddPlayerSchema
from app.database.models.card import CardOrm
from app.database.models.health import HealthOrm
from app.database.models.player import PlayerOrm
from app.utils.repository import AbsRepo


class PlayerRepository(AbsRepo):
    async def add_one(self, data: AddPlayerSchema) -> None:
        player = PlayerOrm(**data.model_dump())
        self.session.add(player)
        await self.session.commit()

    async def get_all(self) -> list[PlayerOrm]:
        query = (
            select(PlayerOrm)
            .options(selectinload(PlayerOrm.card)
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
        )
        return await self.session.scalars(query)
