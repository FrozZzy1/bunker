from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas.genderage import AddGenderageSchema, ReadGenderageSchema
from app.database.database import get_session
from app.services.genderage import GenderageService

genderage_router = APIRouter(
    prefix='/genderages',
    tags=['Genderages'],
)


@genderage_router.post(
    '',
    status_code=status.HTTP_201_CREATED,
)
async def create_genderage(
    genderage: AddGenderageSchema,
    session: AsyncSession = Depends(get_session),
):
    genderage_service = GenderageService(session)
    await genderage_service.create_genderage(genderage)


@genderage_router.get(
    '',
    response_model=list[ReadGenderageSchema],
)
async def get_all_genderages(session: AsyncSession = Depends(get_session)):
    genderage_service = GenderageService(session)
    genderages = await genderage_service.get_all_genderages()
    return genderages
