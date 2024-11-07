from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas.room import AddRoomSchema
from app.database.models.room import RoomOrm


class RoomRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def add_one(self, data: AddRoomSchema) -> None:
        room = RoomOrm(**data.model_dump())
        self.session.add(room)
        await self.session.commit()
        await self.session.refresh(room)

    async def get_all(self) -> list[RoomOrm]:
        query = (
            select(RoomOrm)
            .options(
                selectinload(RoomOrm.players)
            )
        )
        result = await self.session.scalars(query)
        return result
