from pydantic import BaseModel


class ReadProfessionSchema(BaseModel):
    id: int
    title: str


class AddProfessionSchema(BaseModel):
    title: str


class UpdateProfessionSchema(BaseModel):
    title: str
