from pydantic import BaseModel


class ReadPhobiaSchema(BaseModel):
    id: int
    title: str


class AddPhobiaSchema(BaseModel):
    title: str


class UpdatePhobiaSchema(BaseModel):
    title: str
