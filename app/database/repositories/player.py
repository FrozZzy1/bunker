from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas.player import AddPlayerSchema
from app.database.models.card import CardOrm
from app.database.models.player import PlayerOrm


class PlayerRepository(AbsRepo):
    async def add_one(self, data: AddPlayerSchema) -> None:
        player = PlayerOrm(**data.model_dump())
        self.session.add(player)
        await self.session.commit()

    async def get_all(self) -> list[PlayerOrm]:
        query = (
            select(PlayerOrm)
            .options(selectinload(PlayerOrm.card)
            .options(selectinload(CardOrm.profession))
            )
        )
        result = await self.session.scalars(query)
        return result
