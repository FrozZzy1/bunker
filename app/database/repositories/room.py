from sqlalchemy import select

from app.api.schemas.room import AddRoomSchema, ReadRoomSchema
from app.database.models.room import RoomOrm
from app.utils.repository import AbsRepo


class RoomRepository(AbsRepo):
    async def add_one(self, data: AddRoomSchema) -> ReadRoomSchema:
        room = RoomOrm(**data.model_dump())
        self.session.add(room)
        await self.session.commit()
        await self.session.refresh(room)
        return ReadRoomSchema.model_validate(room)

    async def get_all(self) -> list[ReadRoomSchema]:
        query = select(RoomOrm)
        result = await self.session.scalars(query)
        return [ReadRoomSchema.model_validate(i) for i in result]
