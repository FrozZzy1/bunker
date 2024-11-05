from typing import Literal

from pydantic import BaseModel


class ReadGenderageSchema(BaseModel):
    id: int
    gender: str
    age: int


class AddGenderageSchema(BaseModel):
    gender: Literal['мужчина', 'женщина']
    age: int
