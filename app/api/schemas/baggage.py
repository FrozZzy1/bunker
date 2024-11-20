from pydantic import BaseModel, ConfigDict


class ReadBaggageSchema(BaseModel):
    id: int
    title: str

    model_config = ConfigDict(from_attributes=True)


class AddBaggageSchema(BaseModel):
    title: str
