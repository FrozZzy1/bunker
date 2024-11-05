from pydantic import BaseModel


class ReadHobbySchema(BaseModel):
    id: int
    title: str


class AddHobbySchema(BaseModel):
    title: str
