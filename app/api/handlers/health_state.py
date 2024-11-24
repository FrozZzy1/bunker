from fastapi import APIRouter, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas.response import ResponseSchema
from app.api.schemas.health import AddHealthStateSchema
from app.database.database import get_session
from app.services.health_state import HealthStateService

health_states_router = APIRouter(
    prefix='/health_states',
    tags=['Health States'],
)


@health_states_router.post(
    '',
    status_code=status.HTTP_201_CREATED,
    response_model=ResponseSchema,
)
async def create_health_state(
    health_state: AddHealthStateSchema,
    session: AsyncSession = Depends(get_session),
):
    health_state_service = HealthStateService(session)
    return await health_state_service.create_health_state(health_state)


@health_states_router.get(
    '',
    response_model=ResponseSchema,
)
async def get_all_health_states(session: AsyncSession = Depends(get_session)):
    health_state_service = HealthStateService(session)
    health_state = await health_state_service.get_all_health_states()
    return health_state


