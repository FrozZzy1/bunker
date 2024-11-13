from fastapi import APIRouter, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas.baggage import ReadBaggageSchema, AddBaggageSchema # noqa
from app.services.baggage import BaggageService
from app.database.database import get_session

baggages_router = APIRouter(
    prefix='/baggages',
    tags=['Baggages'],
)


@baggages_router.post(
    '',
    status_code=status.HTTP_201_CREATED,
)
async def create_baggage(
    baggage: AddBaggageSchema,
    session: AsyncSession = Depends(get_session),
):
    baggage_service = BaggageService(session)
    await baggage_service.create_profession(baggage)


@baggages_router.get(
    '',
    response_model=list[ReadBaggageSchema],
)
async def get_all_baggages(session: AsyncSession = Depends(get_session)):
    baggage_service = BaggageService(session)
    baggages = await baggage_service.get_all_baggages()
    return baggages
