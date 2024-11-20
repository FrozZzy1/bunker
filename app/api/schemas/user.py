from pydantic import BaseModel, ConfigDict
from datetime import datetime


class ReadUserSchema(BaseModel):
    id: int
    tg_id: int
    name: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class AddUserSchema(BaseModel):
    tg_id: int
    name: str


class UpdateUserSchema(BaseModel):
    name: str
