from sqlalchemy import select

from app.api.schemas.trait import AddTraitSchema, ReadTraitSchema
from app.database.models.trait import TraitOrm
from app.utils.repository import AbsRepo


class TraitRepository(AbsRepo):
    async def add_one(self, data: AddTraitSchema) -> ReadTraitSchema:
        trait = TraitOrm(**data.model_dump())
        self.session.add(trait)
        await self.session.commit()
        await self.session.refresh(trait)
        return ReadTraitSchema.model_validate(trait)

    async def get_all(self) -> list[ReadTraitSchema]:
        query = select(TraitOrm)
        result = await self.session.scalars(query)
        return [ReadTraitSchema.model_validate(i) for i in result]
    
    async def get_all_id(self) -> list[int]:
        query = select(TraitOrm.id)
        result = await self.session.scalars(query)
        return list(result)
