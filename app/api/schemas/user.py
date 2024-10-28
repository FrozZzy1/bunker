from pydantic import BaseModel


class ReadUserSchema(BaseModel):
    id: int
    tg_username: str
    name: str


class AddUserSchema(BaseModel):
    tg_username: str
    name: str


class UpdateUserSchema(BaseModel):
    tg_username: str
    name: str
