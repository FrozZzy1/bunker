from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas.phobia import AddPhobiaSchema, ReadPhobiaSchema
from app.database.database import get_session
from app.services.phobia import PhobiaService

phobias_router = APIRouter(
    prefix='/phobias',
    tags=['Phobias'],
)


@phobias_router.post(
    '',
    status_code=status.HTTP_201_CREATED,
)
async def create_phobia(
    phobia: AddPhobiaSchema,
    session: AsyncSession = Depends(get_session),
):
    phobia_service = PhobiaService(session)
    await phobia_service.create_phobia(phobia)


@phobias_router.get(
    '',
    response_model=list[ReadPhobiaSchema],
)
async def get_all_phobias(session: AsyncSession = Depends(get_session)):
    phobia_service = PhobiaService(session)
    return await phobia_service.get_all_phobias()
