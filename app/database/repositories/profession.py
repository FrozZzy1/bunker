from sqlalchemy import select

from app.database.database import async_session_maker
from app.database.models.profession import ProfessionOrm


class ProfessionRepository:
    @staticmethod
    async def add_one(data: dict) -> None:
        async with async_session_maker() as session:
            profession = ProfessionOrm(**data)
            session.add(profession)
            await session.commit()
            await session.refresh(profession)

    @staticmethod
    async def get_all() -> list[ProfessionOrm]:
        async with async_session_maker() as session:
            query = select(ProfessionOrm)
            result = await session.scalars(query)
            return result
