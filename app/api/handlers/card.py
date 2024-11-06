from fastapi import APIRouter, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas.card import ReadCardSchema, AddCardSchema
from app.services.card import CardService
from app.database.database import get_session

cards_router = APIRouter(
    prefix='/cards',
    tags=['Cards'],
)


@cards_router.post(
    '',
    status_code=status.HTTP_201_CREATED,
)
async def create_card(
    card: AddCardSchema,
    session: AsyncSession = Depends(get_session),
):
    await CardService.create_card(session, card)


@cards_router.get(
    '',
    response_model=list[ReadCardSchema],
)
async def get_all_cards(session: AsyncSession = Depends(get_session)):
    cards = await CardService.get_all_cards(session)
    return cards
