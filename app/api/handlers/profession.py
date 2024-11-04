from fastapi import APIRouter, status

from app.api.schemas.profession import ReadProfessionSchema, AddProfessionSchema # noqa
from app.services.profession import ProfessionService

professions_router = APIRouter(
    prefix='/professions',
    tags=['Professions'],
)


@professions_router.post(
    '',
    status_code=status.HTTP_201_CREATED,
)
async def create_profession(
    profession: AddProfessionSchema,
):
    await ProfessionService.create_profession(profession)


@professions_router.get(
    '',
    response_model=list[ReadProfessionSchema],
)
async def get_all_professions():
    professions = await ProfessionService.get_all_professions()
    return professions
