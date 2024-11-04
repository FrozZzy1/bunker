from pydantic import BaseModel

from app.api.schemas.profession import ReadProfessionSchema


class ReadCardSchema(BaseModel):
    id: int
    profession: ReadProfessionSchema


class AddCardSchema(BaseModel):
    profession_id: int
