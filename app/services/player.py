from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas.player import AddPlayerSchema, ReadPlayerSchema
from app.api.schemas.response import ResponseSchema
from app.database.repositories.player import PlayerRepository


class PlayerService:
    def __init__(self, session: AsyncSession) -> None:
        self.player_repository = PlayerRepository(session)

    async def create_player(self, player: AddPlayerSchema) -> ResponseSchema:
        player = await self.player_repository.add_one(player)
        return ResponseSchema(
            data=player.model_dump(),
            messages=[f'Player with id={player.id} added successfully'],
        )

    async def get_all_players(self) -> list[ReadPlayerSchema]:
        players = await self.player_repository.get_all()
        return players
