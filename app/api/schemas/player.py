from pydantic import BaseModel
from datetime import datetime


class ReadPlayerSchema(BaseModel):
    id: int
    user_id: int
    card_id: int
    created_at: datetime


class AddPlayerSchema(BaseModel):
    user_id: int
    card_id: int | None = None
