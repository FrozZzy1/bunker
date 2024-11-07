from fastapi import APIRouter, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas.player import ReadPlayerSchema, AddPlayerSchema
from app.services.player import PlayerService
from app.database.database import get_session

players_router = APIRouter(
    prefix='/players',
    tags=['Players'],
)


@players_router.post(
    '',
    status_code=status.HTTP_201_CREATED,
)
async def create_player(
    player: AddPlayerSchema,
    session: AsyncSession = Depends(get_session)
):
    player_service = PlayerService(session)
    await player_service.create_player(player)


@players_router.get(
    '',
    response_model=list[ReadPlayerSchema],
)
async def get_all_players(session: AsyncSession = Depends(get_session)):
    player_service = PlayerService(session)
    players = await player_service.get_all_players()
    return players
