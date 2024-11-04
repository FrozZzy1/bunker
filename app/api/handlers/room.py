from fastapi import APIRouter, status

from app.api.schemas.room import ReadRoomSchema, AddRoomSchema
from app.services.room import RoomService

rooms_router = APIRouter(
    prefix='/rooms',
    tags=['Rooms'],
)


@rooms_router.post(
    '',
    status_code=status.HTTP_201_CREATED,
)
async def create_room(
    room: AddRoomSchema,
):
    await RoomService.create_room(room)


@rooms_router.get(
    '',
    response_model=list[ReadRoomSchema],
)
async def get_all_rooms():
    rooms = await RoomService.get_all_rooms()
    return rooms
