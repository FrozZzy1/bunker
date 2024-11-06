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
    await UserService.create_user(session, user)


@users_router.get(
    '',
    response_model=list[ReadUserSchema],
)
async def get_all_users(session: AsyncSession = Depends(get_session)):
    users = await UserService.get_all_users(session)
    return users
