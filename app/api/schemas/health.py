from pydantic import BaseModel


class ReadHealthSchema(BaseModel):
    id: int
    health_title_id: int
    health_state_id: int


class AddHealthSchema(BaseModel):
    health_title_id: int
    health_state_id: int


class UpdateHealthSchema(BaseModel):
    health_title_id: int | None = None
    health_state_id: int | None = None
