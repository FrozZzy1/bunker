from pydantic import BaseModel


class ReadBaggageSchema(BaseModel):
    id: int
    title: str


class AddBaggageSchema(BaseModel):
    title: str


class UpdateBaggageSchema(BaseModel):
    title: str
