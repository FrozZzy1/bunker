from pydantic import BaseModel


class ReadRoomSchema(BaseModel):
    id: int
    players: int
    players_id: list[int]
    state: int


class AddRoomSchema(BaseModel):
    players: int
    players_id: list[int]
    state: int = 0


class UpdateRoomSchema(BaseModel):
    player_id: int | None = None
    state: int | None = None
