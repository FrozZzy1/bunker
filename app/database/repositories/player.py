from sqlalchemy import select
from sqlalchemy.orm import selectinload, joinedload

from app.api.schemas.player import AddPlayerSchema, ReadPlayerSchema
from app.database.models.card import CardOrm
from app.database.models.health import HealthOrm
from app.database.models.player import PlayerOrm
from app.utils.repository import AbsRepo


class PlayerRepository(AbsRepo):
    async def add_one(self, data: AddPlayerSchema) -> ReadPlayerSchema:
        player = PlayerOrm(**data.model_dump())
        self.session.add(player)
        await self.session.commit()
        await self.session.refresh(player)
        return ReadPlayerSchema.model_validate(player)

    async def get_all(self) -> list[ReadPlayerSchema]:
        query = select(PlayerOrm)
        result = await self.session.scalars(query)
        return [ReadPlayerSchema.model_validate(i) for i in result]
