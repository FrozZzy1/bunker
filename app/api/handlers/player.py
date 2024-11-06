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
    await PlayerService.create_player(session, player)


@players_router.get(
    '',
    response_model=list[ReadPlayerSchema],
)
async def get_all_players(session: AsyncSession = Depends(get_session)):
    players = await PlayerService.get_all_players(session)
    return players
