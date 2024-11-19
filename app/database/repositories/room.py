from sqlalchemy import select
from sqlalchemy.orm import selectinload, joinedload

from app.api.schemas.room import AddRoomSchema
from app.database.models.card import CardOrm
from app.database.models.player import PlayerOrm
from app.database.models.room import RoomOrm
from app.database.models.health import HealthOrm
from app.utils.repository import AbsRepo


class RoomRepository(AbsRepo):
    async def add_one(self, data: AddRoomSchema) -> RoomOrm:
        room = RoomOrm(**data.model_dump())
        self.session.add(room)
        await self.session.commit()
        await self.session.refresh(room)
        return room

    async def get_all(self) -> list[RoomOrm]:
        query = select(RoomOrm)
        return await self.session.scalars(query)
