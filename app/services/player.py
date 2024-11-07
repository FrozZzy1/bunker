from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas.player import AddPlayerSchema
from app.database.models.player import PlayerOrm
from app.database.repositories.player import PlayerRepository


class PlayerService:
    def __init__(self, session: AsyncSession) -> None:
        self.player_repository = PlayerRepository(session)

    async def create_player(self, player: AddPlayerSchema) -> None:
        await self.player_repository.add_one(player)

    async def get_all_players(self) -> list[PlayerOrm]:
        players = await self.player_repository.get_all()
        return players
