from pydantic import BaseModel


class ReadTraitSchema(BaseModel):
    id: int
    title: str


class AddTraitSchema(BaseModel):
    title: str


class UpdateTraitSchema(BaseModel):
    title: str
