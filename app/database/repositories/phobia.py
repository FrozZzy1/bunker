from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas.phobia import AddPhobiaSchema
from app.database.models.phobia import PhobiaOrm


class PhobiaRepository(AbsRepo):
    async def add_one(self, data: AddPhobiaSchema) -> None:
        phobia = PhobiaOrm(**data.model_dump())
        self.session.add(phobia)
        await self.session.commit()

    async def get_all_phobias(self) -> list[PhobiaOrm]:
        query = select(PhobiaOrm)
        result = await self.session.scalars(query)
        return result
