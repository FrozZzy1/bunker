from fastapi import APIRouter, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas.health import AddHealthSchema, ReadHealthSchema
from app.database.database import get_session
from app.services.health import HealthService

health_router = APIRouter(
    prefix='/health',
    tags=['Health'],
)


@health_router.post(
    '',
    status_code=status.HTTP_201_CREATED,
)
async def create_health(
    health: AddHealthSchema,
    session: AsyncSession = Depends(get_session),
):
    health_service = HealthService(session)
    await health_service.create_health(health)


@health_router.get(
    '',
    response_model=list[ReadHealthSchema],
)
async def get_all_health(session: AsyncSession = Depends(get_session)):
    health_service = HealthService(session)
    health = await health_service.get_all_health()
    return health


