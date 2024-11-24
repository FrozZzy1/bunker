from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas.response import ResponseSchema
from app.api.schemas.phobia import AddPhobiaSchema
from app.database.database import get_session
from app.services.phobia import PhobiaService

phobias_router = APIRouter(
    prefix='/phobias',
    tags=['Phobias'],
)


@phobias_router.post(
    '',
    status_code=status.HTTP_201_CREATED,
    response_model=ResponseSchema,
)
async def create_phobia(
    phobia: AddPhobiaSchema,
    session: AsyncSession = Depends(get_session),
):
    phobia_service = PhobiaService(session)
    return await phobia_service.create_phobia(phobia)


@phobias_router.get(
    '',
    response_model=ResponseSchema,
)
async def get_all_phobias(session: AsyncSession = Depends(get_session)):
    phobia_service = PhobiaService(session)
    return await phobia_service.get_all_phobias()
