from fastapi import APIRouter, status

from app.api.schemas.player import ReadPlayerSchema, AddPlayerSchema
from app.services.player import PlayerService

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
):
    await PlayerService.create_player(player)


@players_router.get(
    '',
    response_model=list[ReadPlayerSchema],
)
async def get_all_players():
    players = await PlayerService.get_all_players()
    return players
