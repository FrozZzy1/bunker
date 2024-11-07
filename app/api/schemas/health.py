from pydantic import BaseModel


class ReadHealthTitleSchema(BaseModel):
    id: int
    title: str


class AddHealthTitleSchema(BaseModel):
    title: str


class ReadHealthStateSchema(BaseModel):
    id: int
    title: str


class AddHealthStateSchema(BaseModel):
    title: str


class ReadHealthSchema(BaseModel):
    id: int
    health_title: ReadHealthTitleSchema
    health_state: ReadHealthStateSchema


class AddHealthSchema(BaseModel):
    health_title_id: int
    health_state_id: int
