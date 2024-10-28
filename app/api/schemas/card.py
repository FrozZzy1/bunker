from pydantic import BaseModel


class ReadCardSchema(BaseModel):
    id: int
    health_id: int
    profession_id: int
    phobia_id: int
    baggage_id: int
    hobby_id: int
    trait_id: int
    physique_id: int
    genderage_id: int
    action_card_id: int


class AddCardSchema(BaseModel):
    health_id: int
    profession_id: int
    phobia_id: int
    baggage_id: int
    hobby_id: int
    trait_id: int
    physique_id: int
    genderage_id: int
    action_card_id: int


class UpdateCardSchema(BaseModel):
    health_id: int | None = None
    profession_id: int | None = None
    phobia_id: int | None = None
    baggage_id: int | None = None
    hobby_id: int | None = None
    trait_id: int | None = None
    physique_id: int | None = None
    genderage_id: int | None = None
    action_card_id: int | None = None
