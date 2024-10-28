from pydantic import BaseModel


class ReadPlayerSchema(BaseModel):
    id: int
    user_id: int
    card_id: int


class AddPlayerSchema(BaseModel):
    user_id: int
    card_id: int | None = None
