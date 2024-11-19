from pydantic import BaseModel

from app.api.schemas.player import ReadPlayerSchema


class ReadRoomSchema(BaseModel):
    id: int
    code: str
    capacity: int
    state: int


class AddRoomSchema(BaseModel):
    code: str | None = None
    capacity: int
    state: int = 0


class UpdateRoomSchema(BaseModel):
    player_id: int | None = None
    state: int | None = None
