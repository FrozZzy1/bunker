from fastapi import APIRouter, status

from app.api.schemas.card import ReadCardSchema, AddCardSchema
from app.services.card import CardService

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
):
    await CardService.create_card(card)


@cards_router.get(
    '',
    response_model=list[ReadCardSchema],
)
async def get_all_cards():
    cards = await CardService.get_all_cards()
    return cards
