from fastapi import APIRouter, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas.response import ResponseSchema
from app.api.schemas.user import AddUserSchema, UpdateUserSchema
from app.database.database import get_session
from app.services.user import UserService

users_router = APIRouter(
    prefix='/users',
    tags=['Users'],
)


@users_router.post(
    '',
    status_code=status.HTTP_201_CREATED,
    response_model=ResponseSchema,
)
async def create_user(
    user: AddUserSchema,
    session: AsyncSession = Depends(get_session),
):
    user_service = UserService(session)
    return await user_service.create_user(user)


@users_router.get(
    '',
    response_model=ResponseSchema,
)
async def get_all_users(session: AsyncSession = Depends(get_session)):
    user_service = UserService(session)
    users = await user_service.get_all_users()
    return users


@users_router.patch(
    '/{tg_id}',
    response_model=ResponseSchema,
)
async def update_user(
    tg_id: int,
    user: UpdateUserSchema,
    session: AsyncSession = Depends(get_session)
):
    user_service = UserService(session)
    user = await user_service.update_user(tg_id, user)
    return user
