from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas.player import AddPlayerSchema
from app.database.models.player import PlayerOrm
from app.database.repositories.player import PlayerRepository


class PlayerService:
    @classmethod
    async def create_player(cls, session: AsyncSession, player: AddPlayerSchema) -> None:
        await PlayerRepository.add_one(session, player)

    @classmethod
    async def get_all_players(cls, session: AsyncSession) -> list[PlayerOrm]:
        players = await PlayerRepository.get_all(session)
        return players
