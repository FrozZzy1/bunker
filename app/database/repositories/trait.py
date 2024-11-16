from sqlalchemy import select

from app.api.schemas.trait import AddTraitSchema
from app.database.models.trait import TraitOrm
from app.utils.repository import AbsRepo


class TraitRepository(AbsRepo):
    async def add_one(self, data: AddTraitSchema) -> None:
        trait = TraitOrm(**data.model_dump())
        self.session.add(trait)
        await self.session.commit()

    async def get_all_traits(self) -> list[TraitOrm]:
        query = select(TraitOrm)
        return await self.session.scalars(query)
