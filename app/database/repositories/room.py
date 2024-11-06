from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas.room import AddRoomSchema
from app.database.models.room import RoomOrm


class RoomRepository:
    @classmethod
    async def add_one(cls, session: AsyncSession, data: AddRoomSchema) -> None:
        room = RoomOrm(**data.model_dump())
        session.add(room)
        await session.commit()
        await session.refresh(room)

    @classmethod
    async def get_all(cls, session: AsyncSession) -> list[RoomOrm]:
        query = (
            select(RoomOrm)
            .options(
                selectinload(RoomOrm.players)
            )
        )
        result = await session.scalars(query)
        return result
