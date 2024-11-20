from sqlalchemy import select

from app.api.schemas.physique import AddPhysiqueSchema, ReadPhysiqueSchema
from app.database.models.physique import PhysiqueOrm
from app.utils.repository import AbsRepo


class PhysiqueRepository(AbsRepo):
    async def add_one(self, data: AddPhysiqueSchema) -> None:
        physique = PhysiqueOrm(**data.model_dump())
        self.session.add(physique)
        await self.session.commit()

    async def get_all(self) -> list[ReadPhysiqueSchema]:
        query = select(PhysiqueOrm)
        result = await self.session.scalars(query)
        return [ReadPhysiqueSchema.model_validate(i) for i in result]
    
    async def get_all_id(self) -> list[int]:
        query = select(PhysiqueOrm.id)
        result = await self.session.scalars(query)
        return list(result)