from fastapi import APIRouter, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas.response import ResponseSchema
from app.api.schemas.room import AddRoomSchema
from app.services.room import RoomService
from app.database.database import get_session

rooms_router = APIRouter(
    prefix='/rooms',
    tags=['Rooms'],
)


@rooms_router.post(
    '',
    status_code=status.HTTP_201_CREATED,
    response_model=ResponseSchema,
)
async def create_room(
    room: AddRoomSchema,
    session: AsyncSession = Depends(get_session),
):
    room_service = RoomService(session)
    return await room_service.create_room(room)


@rooms_router.get(
    '',
    response_model=ResponseSchema,
)
async def get_all_rooms(session: AsyncSession = Depends(get_session)):
    room_service = RoomService(session)
    rooms = await room_service.get_all_rooms()
    return rooms
