from sqlalchemy import select

from app.api.schemas.profession import AddProfessionSchema, ReadProfessionSchema
from app.database.models.profession import ProfessionOrm
from app.utils.repository import AbsRepo


class ProfessionRepository(AbsRepo):
    async def add_one(self, data: AddProfessionSchema) -> None:
        profession = ProfessionOrm(**data.model_dump())
        self.session.add(profession)
        await self.session.commit()

    async def get_all(self) -> list[ReadProfessionSchema]:
        query = select(ProfessionOrm)
        result = await self.session.scalars(query)
        return [ReadProfessionSchema.model_validate(i) for i in result]
    
    async def get_all_id(self) -> list[int]:
        query = select(ProfessionOrm.id)
        result = await self.session.scalars(query)
        return list(result)