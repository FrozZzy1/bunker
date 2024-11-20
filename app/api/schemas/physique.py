from pydantic import BaseModel, ConfigDict


class ReadPhysiqueSchema(BaseModel):
    id: int
    title: str

    model_config = ConfigDict(from_attributes=True)


class AddPhysiqueSchema(BaseModel):
    title: str
