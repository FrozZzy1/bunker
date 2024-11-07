from typing import Literal

from enum import Enum
from pydantic import BaseModel


class ReadGenderageSchema(BaseModel):
    id: int
    gender: str
    age: int


class GenderEnum(str, Enum):
    man = 'мужчина'
    woman = 'женщина'


class AddGenderageSchema(BaseModel):
    gender: GenderEnum = GenderEnum.man
    age: int
