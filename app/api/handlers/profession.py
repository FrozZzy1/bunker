from fastapi import APIRouter, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas.profession import ReadProfessionSchema, AddProfessionSchema # noqa
from app.services.profession import ProfessionService
from app.database.database import get_session

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
    session: AsyncSession = Depends(get_session),
):
    await ProfessionService.create_profession(session, profession)


@professions_router.get(
    '',
    response_model=list[ReadProfessionSchema],
)
async def get_all_professions(session: AsyncSession = Depends(get_session)):
    professions = await ProfessionService.get_all_professions(session)
    return professions
