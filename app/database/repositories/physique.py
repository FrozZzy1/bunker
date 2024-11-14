from sqlalchemy import select

from app.api.schemas.physique import AddPhysiqueSchema
from app.database.models.physique import PhysiqueOrm
from app.utils.repository import AbsRepo


class PhysiqueRepository(AbsRepo):
    async def add_one(self, data: AddPhysiqueSchema) -> None:
        physique = PhysiqueOrm(**data.model_dump())
        self.session.add(physique)
        await self.session.commit()

    async def get_all_physique(self) -> list[PhysiqueOrm]:
        query = select(PhysiqueOrm)
        result = await self.session.scalars(query)
        return result
