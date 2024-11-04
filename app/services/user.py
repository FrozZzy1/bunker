from app.api.schemas.user import AddUserSchema
from app.database.models.user import UserOrm
from app.database.repositories.user import UserRepository


class UserService:
    @classmethod
    async def create_user(cls, user: AddUserSchema) -> None:
        user_dict = user.model_dump()
        await UserRepository.add_one(user_dict)

    @classmethod
    async def get_all_users(cls) -> list[UserOrm]:
        users = await UserRepository.get_all()
        return users
