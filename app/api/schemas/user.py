from pydantic import BaseModel
from datetime import datetime


class ReadUserSchema(BaseModel):
    id: int
    tg_id: str
    tg_username: str
    name: str
    created_at: datetime
    updated_at: datetime


class AddUserSchema(BaseModel):
    tg_id: str
    tg_username: str
    name: str


class UpdateUserSchema(BaseModel):
    tg_username: str
    name: str
