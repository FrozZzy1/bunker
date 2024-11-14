from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas.trait import AddTraitSchema
from app.database.models.trait import TraitOrm
from app.database.repositories.trait import TraitRepository


class TraitService:
    def __init__(self, session: AsyncSession) -> None:
        self.trait_repo = TraitRepository(session)

    async def create_trait(self, trait: AddTraitSchema) -> None:
        await self.trait_repo.add_one(trait)

    async def get_all_traits(self) -> list[TraitOrm]:
        traits = await self.trait_repo.get_all_traits()
        return traits
