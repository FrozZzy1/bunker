from fastapi import APIRouter, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas.room import ReadRoomSchema, AddRoomSchema
from app.services.room import RoomService
from app.database.database import get_session

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
    session: AsyncSession = Depends(get_session),
):
    room_service = RoomService(session)
    await room_service.create_room(room)


@rooms_router.get(
    '',
    response_model=list[ReadRoomSchema],
)
async def get_all_rooms(session: AsyncSession = Depends(get_session)):
    room_service = RoomService(session)
    rooms = await room_service.get_all_rooms()
    return rooms
