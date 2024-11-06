from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.models.player import PlayerOrm


class PlayerRepository:
    @classmethod
    async def add_one(cls, session: AsyncSession, data: dict) -> None:
        player = PlayerOrm(**data.model_dump())
        session.add(player)
        await session.commit()
        await session.refresh(player)

    @classmethod
    async def get_all(cls, session: AsyncSession) -> list[PlayerOrm]:
        query = select(PlayerOrm)
        result = await session.scalars(query)
        return result
