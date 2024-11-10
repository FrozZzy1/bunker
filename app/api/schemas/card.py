from pydantic import BaseModel

from app.api.schemas.baggage import ReadBaggageSchema
from app.api.schemas.genderage import ReadGenderageSchema
from app.api.schemas.health import ReadHealthSchema
from app.api.schemas.hobby import ReadHobbySchema
from app.api.schemas.phobia import ReadPhobiaSchema
from app.api.schemas.physique import ReadPhysiqueSchema
from app.api.schemas.profession import ReadProfessionSchema
from app.api.schemas.trait import ReadTraitSchema


class ReadCardSchema(BaseModel):
    id: int
    health: ReadHealthSchema
    profession: ReadProfessionSchema
    phobia: ReadPhobiaSchema
    # baggage: ReadBaggageSchema
    # hobby: ReadHobbySchema
    # trait: ReadTraitSchema
    # physique: ReadPhysiqueSchema
    # genderage: ReadGenderageSchema


class AddCardSchema(BaseModel):
    health_id: int
    profession_id: int
    phobia_id: int
    # baggage_id: int
    # hobby_id: int
    # trait_id: int
    # physique_id: int
    # genderage_id: int
