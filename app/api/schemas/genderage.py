from pydantic import BaseModel


class ReadGenderageSchema(BaseModel):
    id: int
    gender: str
    age: int


class AddGenderageSchema(BaseModel):
    gender: str
    age: int


class UpdateGenderageSchema(BaseModel):
    gender: str | None = None
    age: int | None = None
