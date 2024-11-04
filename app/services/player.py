from app.api.schemas.player import AddPlayerSchema
from app.database.models.player import PlayerOrm
from app.database.repositories.player import PlayerRepository


class PlayerService:
    @classmethod
    async def create_player(cls, card: AddPlayerSchema) -> None:
        player_dict = card.model_dump()
        await PlayerRepository.add_one(player_dict)

    @classmethod
    async def get_all_players(cls) -> list[PlayerOrm]:
        players = await PlayerRepository.get_all()
        return players
