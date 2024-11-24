from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas.response import ResponseSchema
from app.api.schemas.hobby import AddHobbySchema
from app.database.database import get_session
from app.services.hobby import HobbyService

hobby_router = APIRouter(
    prefix='/hobbies',
    tags=['Hobbies'],
)


@hobby_router.post(
    '',
    status_code=status.HTTP_201_CREATED,
    response_model=ResponseSchema,
)
async def create_hobby(
    hobby: AddHobbySchema,
    session: AsyncSession = Depends(get_session),
):
    hobby_service = HobbyService(session)
    return await hobby_service.create_hobby(hobby)


@hobby_router.get(
    '',
    response_model=ResponseSchema,
)
async def get_all_hobbies(session: AsyncSession = Depends(get_session)):
    hobby_service = HobbyService(session)
    hobbies = await hobby_service.get_all_hobbies()
    return hobbies
