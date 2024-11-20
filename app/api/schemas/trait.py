from pydantic import BaseModel, ConfigDict


class ReadTraitSchema(BaseModel):
    id: int
    title: str

    model_config = ConfigDict(from_attributes=True)


class AddTraitSchema(BaseModel):
    title: str
