from app.api.schemas.user import AddUserSchema
from app.database.models.user import UserOrm
from app.database.repositories.user import UserRepository


class UserService:
    @classmethod
    async def create_user(cls, user: AddUserSchema) -> UserOrm:
        user_dict = user.model_dump()
        user = await UserRepository.add_user(user_dict)
        return user

    @classmethod
    async def get_users(cls) -> list[UserOrm]:
        users = await UserRepository.get_users()
        return users
