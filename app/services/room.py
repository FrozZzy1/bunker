from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas.room import AddRoomSchema
from app.database.models.room import RoomOrm
from app.database.repositories.room import RoomRepository
from app.utils.room_code import generate_room_code


class RoomService:
    @classmethod
    async def create_room(cls, session: AsyncSession, room: AddRoomSchema) -> None:
        room.code = await generate_room_code()
        await RoomRepository.add_one(session, room)

    @classmethod
    async def get_all_rooms(cls, session: AsyncSession) -> list[RoomOrm]:
        rooms = await RoomRepository.get_all(session)
        return rooms
