from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.models.profession import ProfessionOrm


class ProfessionRepository:
    @classmethod
    async def add_one(cls, session: AsyncSession, data: dict) -> None:
        profession = ProfessionOrm(**data.model_dump())
        session.add(profession)
        await session.commit()
        await session.refresh(profession)

    @classmethod
    async def get_all(cls, session: AsyncSession) -> list[ProfessionOrm]:
        query = select(ProfessionOrm)
        result = await session.scalars(query)
        return result
