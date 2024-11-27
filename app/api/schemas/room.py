from pydantic import BaseModel, ConfigDict

from app.api.schemas.player import ReadPlayerSchema


class ReadRoomSchema(BaseModel):
    id: int
    code: str
    capacity: int
    state: int

    model_config = ConfigDict(from_attributes=True)


class AddRoomSchema(BaseModel):
    code: str | None = None
    capacity: int
    state: int = 0


class UpdateRoomSchema(BaseModel):
    id: int
    state: int
