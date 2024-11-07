from fastapi import APIRouter, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas.health import AddHealthTitleSchema, ReadHealthTitleSchema
from app.database.database import get_session
from app.services.health_title import HealthTitleService

health_titles_router = APIRouter(
    prefix='/health_titles',
    tags=['Health Titles'],
)


@health_titles_router.post(
    '',
    status_code=status.HTTP_201_CREATED,
)
async def create_health_tilte(
    health_title: AddHealthTitleSchema,
    session: AsyncSession = Depends(get_session),
):
    health_title_service = HealthTitleService(session)
    await health_title_service.create_health_title(health_title)


@health_titles_router.get(
    '',
    response_model=list[ReadHealthTitleSchema],
)
async def get_all_health_titles(session: AsyncSession = Depends(get_session)):
    health_title_service = HealthTitleService(session)
    health = await health_title_service.get_all_health_titles()
    return health


