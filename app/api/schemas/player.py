from pydantic import BaseModel, ConfigDict

from app.api.schemas.card import ReadCardSchema


class ReadPlayerSchema(BaseModel):
    id: int
    user_id: int
    room_id: int
    card_id: int | None

    model_config = ConfigDict(from_attributes=True)


class AddPlayerSchema(BaseModel):
    user_id: int
    room_id: int
    card_id: int | None = None


class UpdatePlayerSchema(BaseModel):
    id: int
    card_id: int
