from pydantic import BaseModel, ConfigDict


class ReadPhobiaSchema(BaseModel):
    id: int
    title: str

    model_config = ConfigDict(from_attributes=True)


class AddPhobiaSchema(BaseModel):
    title: str
