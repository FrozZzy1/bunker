from pydantic import BaseModel


class ReadHealthStateSchema(BaseModel):
    id: int
    title: str


class AddHealthStateSchema(BaseModel):
    title: str


class UpdateHealthStateSchema(BaseModel):
    title: str
