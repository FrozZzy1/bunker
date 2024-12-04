from random import choice
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas.health import AddHealthStateSchema
from app.api.schemas.response import ResponseSchema
from app.database.repositories.health_state import HealthStateRepository


class HealthStateService:
    def __init__(self, session: AsyncSession) -> None:
        self.health_state_repository = HealthStateRepository(session)

    async def create_health_state(self, health_state: AddHealthStateSchema) -> ResponseSchema:
        health_state = await self.health_state_repository.add_one(health_state)
        return ResponseSchema(
            data={'health_state': health_state.model_dump()},
            messages=[f'Health state with id={health_state.id} added successfully'],
        )

    async def get_all_health_states(self) -> ResponseSchema:
        health_states = await self.health_state_repository.get_all()
        data = [i.model_dump() for i in health_states]
        return ResponseSchema(
            data={'health_states': data},
            messages=['All health states retrieved successfully'],
        )
    
    async def get_random_id(self) -> int:
        health_states_id = await self.health_state_repository.get_all_id()
        return choice(health_states_id)
