from app.api.schemas.room import AddRoomSchema
from app.database.models.room import RoomOrm
from app.database.repositories.room import RoomRepository
from app.utils.room_code import generate_room_code


class RoomService:
    @classmethod
    async def create_room(cls, room: AddRoomSchema) -> None:
        room_dict = room.model_dump()
        room_dict['code'] = generate_room_code()
        await RoomRepository.add_one(room_dict)

    @classmethod
    async def get_all_rooms(cls) -> list[RoomOrm]:
        rooms = await RoomRepository.get_all()
        return rooms
