from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas.response import ResponseSchema
from app.api.schemas.trait import AddTraitSchema
from app.database.database import get_session
from app.services.trait import TraitService

traits_router = APIRouter(
    prefix='/traits',
    tags=['Traits'],
)


@traits_router.post(
    '',
    status_code=status.HTTP_201_CREATED,
    response_model=ResponseSchema,
)
async def create_trait(
    trait: AddTraitSchema,
    session: AsyncSession = Depends(get_session)
):
    trait_service = TraitService(session)
    return await trait_service.create_trait(trait)


@traits_router.get(
    '',
    response_model=ResponseSchema,
)
async def get_all_traits(session: AsyncSession = Depends(get_session)):
    trait_service = TraitService(session)
    return await trait_service.get_all_traits()
