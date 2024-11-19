from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas.room import AddRoomSchema
from app.database.models.room import RoomOrm
from app.database.repositories.room import RoomRepository
from app.utils.room_code import generate_room_code


class RoomService:
    def __init__(self, session: AsyncSession) -> None:
        self.room_repository = RoomRepository(session)

    async def create_room(self, room: AddRoomSchema) -> None:
        room.code = await generate_room_code()
        return await self.room_repository.add_one(room)

    async def get_all_rooms(self) -> list[RoomOrm]:
        rooms = await self.room_repository.get_all()
        return rooms
