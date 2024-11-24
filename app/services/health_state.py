from random import choice
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas.health import AddHealthStateSchema, ReadHealthStateSchema
from app.api.schemas.response import ResponseSchema
from app.database.repositories.health_state import HealthStateRepository


class HealthStateService:
    def __init__(self, session: AsyncSession) -> None:
        self.health_state_repository = HealthStateRepository(session)

    async def create_health_state(self, health_state: AddHealthStateSchema) -> ResponseSchema:
        health_state = await self.health_state_repository.add_one(health_state)
        return ResponseSchema(
            data=health_state.model_dump(),
            messages=[f'Health state with id={health_state.id} added successfully'],
        )

    async def get_all_health_states(self) -> list[ReadHealthStateSchema]:
        health_state = await self.health_state_repository.get_all()
        return health_state
    
    async def get_random_id(self) -> int:
        health_states_id = await self.health_state_repository.get_all_id()
        return choice(health_states_id)
