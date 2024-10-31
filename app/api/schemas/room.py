from pydantic import BaseModel
from datetime import datetime


class ReadRoomSchema(BaseModel):
    id: int
    code: str
    players: int
    players_id: list[int]
    state: int
    created_at: datetime


class AddRoomSchema(BaseModel):
    code: str
    players: int
    players_id: list[int]
    state: int = 0


class UpdateRoomSchema(BaseModel):
    player_id: int | None = None
    state: int | None = None
