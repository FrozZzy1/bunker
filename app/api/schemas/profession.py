from pydantic import BaseModel, ConfigDict


class ReadProfessionSchema(BaseModel):
    id: int
    title: str

    model_config = ConfigDict(from_attributes=True)


class AddProfessionSchema(BaseModel):
    title: str
