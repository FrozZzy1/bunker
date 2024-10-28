from pydantic import BaseModel


class ReadPhysiqueSchema(BaseModel):
    id: int
    title: str


class AddPhysiqueSchema(BaseModel):
    title: str


class UpdatePhysiqueSchema(BaseModel):
    title: str
