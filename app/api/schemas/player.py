from pydantic import BaseModel


class ReadPlayerSchema(BaseModel):
    id: int
    user_id: int
    card_id: int | None = None
    room_id: int
    # card: ReadCardSchema | None = None


class AddPlayerSchema(BaseModel):
    user_id: int
    room_id: int
    card_id: int | None = None
