from pydantic import BaseModel
from datetime import datetime


class ReadUserSchema(BaseModel):
    id: int
    tg_id: int
    name: str
    created_at: datetime
    updated_at: datetime


class AddUserSchema(BaseModel):
    tg_id: int
    name: str


class UpdateUserSchema(BaseModel):
    name: str
