from fastapi import APIRouter, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas.response import ResponseSchema
from app.api.schemas.player import AddPlayerSchema, UpdatePlayerSchema
from app.services.player import PlayerService
from app.database.database import get_session

players_router = APIRouter(
    prefix='/players',
    tags=['Players'],
)


@players_router.post(
    '',
    status_code=status.HTTP_201_CREATED,
    response_model=ResponseSchema,
)
async def create_player(
    player: AddPlayerSchema,
    session: AsyncSession = Depends(get_session)
):
    player_service = PlayerService(session)
    return await player_service.create_player(player)


@players_router.get(
    '',
    response_model=ResponseSchema,
)
async def get_all_players(session: AsyncSession = Depends(get_session)):
    player_service = PlayerService(session)
    players = await player_service.get_all_players()
    return players


@players_router.patch(
    '',
    response_model=ResponseSchema,
)
async def update_player(
    player: UpdatePlayerSchema,
    session: AsyncSession = Depends(get_session),
):
    player_service = PlayerService(session)
    return await player_service.update_service()
