from sqlalchemy import select
from sqlalchemy.orm import selectinload

from app.database.database import async_session_maker
from app.database.models.room import RoomOrm


class RoomRepository:
    @staticmethod
    async def add_one(data: dict) -> None:
        async with async_session_maker() as session:
            room = RoomOrm(**data)
            session.add(room)
            await session.commit()
            await session.refresh(room)

    @staticmethod
    async def get_all() -> list[RoomOrm]:
        async with async_session_maker() as session:
            query = (
                select(RoomOrm)
                .options(
                    selectinload(RoomOrm.players)
                )
            )
            result = await session.scalars(query)
            return result
