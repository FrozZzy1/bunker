from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas.physique import AddPhysiqueSchema, ReadPhysiqueSchema
from app.database.database import get_session
from app.services.physique import PhysiqueService

physique_router = APIRouter(
    prefix='/physique',
    tags=['Physique'],
)


@physique_router.post(
    '',
    status_code=status.HTTP_201_CREATED,
)
async def create_physique(
    physique: AddPhysiqueSchema,
    session: AsyncSession = Depends(get_session),
):
    physique_service = PhysiqueService(session)
    await physique_service.create_physique(physique)


@physique_router.get(
    '',
    response_model=list[ReadPhysiqueSchema],
)
async def get_all_physique(session: AsyncSession = Depends(get_session)):
    physique_service = PhysiqueService(session)
    physique = await physique_service.get_all_physique()
    return physique
