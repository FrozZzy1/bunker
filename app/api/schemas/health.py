from pydantic import BaseModel, ConfigDict


class ReadHealthTitleSchema(BaseModel):
    id: int
    title: str

    model_config = ConfigDict(from_attributes=True)


class AddHealthTitleSchema(BaseModel):
    title: str


class ReadHealthStateSchema(BaseModel):
    id: int
    title: str

    model_config = ConfigDict(from_attributes=True)


class AddHealthStateSchema(BaseModel):
    title: str


class ReadHealthSchema(BaseModel):
    id: int
    health_title_id: int
    health_state_id: int

    model_config = ConfigDict(from_attributes=True)


class AddHealthSchema(BaseModel):
    health_title_id: int
    health_state_id: int
