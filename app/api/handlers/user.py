from fastapi import APIRouter, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas.user import AddUserSchema, ReadUserSchema, UpdateUserSchema # noqa
from app.database.database import get_session
from app.services.user import UserService

users_router = APIRouter(
    prefix='/users',
    tags=['Users'],
)


@users_router.post(
    '',
    status_code=status.HTTP_201_CREATED,
)
async def create_user(
    user: AddUserSchema,
    session: AsyncSession = Depends(get_session),
):
    user_service = UserService(session)
    await user_service.create_user(user)


@users_router.get(
    '',
    response_model=list[ReadUserSchema],
)
async def get_all_users(session: AsyncSession = Depends(get_session)):
    user_service = UserService(session)
    users = await user_service.get_all_users()
    return users
