from pydantic import BaseModel


class ReadHobbySchema(BaseModel):
    id: int
    title: str


class AddHobbySchema(BaseModel):
    title: str


class UpdateHobbySchema(BaseModel):
    title: str
