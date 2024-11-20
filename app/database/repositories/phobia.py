from sqlalchemy import select

from app.api.schemas.phobia import AddPhobiaSchema, ReadPhobiaSchema
from app.database.models.phobia import PhobiaOrm
from app.utils.repository import AbsRepo


class PhobiaRepository(AbsRepo):
    async def add_one(self, data: AddPhobiaSchema) -> None:
        phobia = PhobiaOrm(**data.model_dump())
        self.session.add(phobia)
        await self.session.commit()

    async def get_all(self) -> list[ReadPhobiaSchema]:
        query = select(PhobiaOrm)
        result = await self.session.scalars(query)
        return [ReadPhobiaSchema.model_validate(i) for i in result]
    
    async def get_all_id(self) -> list[int]:
        query = select(PhobiaOrm.id)
        result = await self.session.scalars(query)
        return list(result)
