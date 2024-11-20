from pydantic import BaseModel, ConfigDict


class ReadHobbySchema(BaseModel):
    id: int
    title: str

    model_config = ConfigDict(from_attributes=True)


class AddHobbySchema(BaseModel):
    title: str
