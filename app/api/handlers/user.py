from fastapi import APIRouter, status

from app.api.schemas.user import AddUserSchema, ReadUserSchema, UpdateUserSchema # noqa
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
):
    user = await UserService.create_user(user)


@users_router.get(
    '',
    response_model=list[ReadUserSchema],
)
async def get_all_users():
    users = await UserService.get_all_users()
    return users
