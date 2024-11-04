from app.api.schemas.profession import AddProfessionSchema
from app.database.models.profession import ProfessionOrm
from app.database.repositories.profession import ProfessionRepository


class ProfessionService:
    @classmethod
    async def create_profession(
        cls,
        profession: AddProfessionSchema,
    ) -> ProfessionOrm:
        profession_dict = profession.model_dump()
        await ProfessionRepository.add_one(profession_dict)

    @classmethod
    async def get_all_professions(cls) -> list[ProfessionOrm]:
        professions = await ProfessionRepository.get_all()
        return professions
