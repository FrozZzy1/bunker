from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas.response import ResponseSchema
from app.api.schemas.room import AddRoomSchema, ReadRoomSchema
from app.database.repositories.room import RoomRepository
from app.utils.room_code import generate_room_code


class RoomService:
    def __init__(self, session: AsyncSession) -> None:
        self.room_repository = RoomRepository(session)

    async def create_room(self, room: AddRoomSchema) -> ResponseSchema:
        room.code = await generate_room_code()
        room = await self.room_repository.add_one(room)
        return ResponseSchema(
            data=room.model_dump(),
            messages=[f'Room with id={room.id} added successfully'],
        )

    async def get_all_rooms(self) -> list[ReadRoomSchema]:
        rooms = await self.room_repository.get_all()
        return rooms
