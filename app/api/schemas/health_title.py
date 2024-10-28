from pydantic import BaseModel


class ReadHealthTitleSchema(BaseModel):
    id: int
    title: str


class AddHealthTitleSchema(BaseModel):
    title: str


class UpdateHealthTitleSchema(BaseModel):
    title: str
