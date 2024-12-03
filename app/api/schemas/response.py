from pydantic import BaseModel


class ResponseSchema(BaseModel):
    data: dict[str, list[dict] | dict] | None = None
    errors: dict[str, list[str]] | None = None
    messages: list[str] | None = None
