from sqlalchemy import select

from app.database.database import async_session_maker
from app.database.models.player import PlayerOrm


class PlayerRepository:
    @staticmethod
    async def add_one(data: dict) -> None:
        async with async_session_maker() as session:
            player = PlayerOrm(**data)
            session.add(player)
            await session.commit()
            await session.refresh(player)

    @staticmethod
    async def get_all() -> list[PlayerOrm]:
        async with async_session_maker() as session:
            query = select(PlayerOrm)
            result = await session.scalars(query)
            return result
