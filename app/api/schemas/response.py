from pydantic import BaseModel


class ResponseSchema(BaseModel):
    data: dict | None = None
    errors: dict | None = None
    messages: list[str] | None = None
