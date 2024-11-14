from sqlalchemy import select
from sqlalchemy.orm import selectinload, joinedload

from app.api.schemas.room import AddRoomSchema
from app.database.models.card import CardOrm
from app.database.models.player import PlayerOrm
from app.database.models.room import RoomOrm
from app.database.models.health import HealthOrm
from app.utils.repository import AbsRepo


class RoomRepository(AbsRepo):
    async def add_one(self, data: AddRoomSchema) -> None:
        room = RoomOrm(**data.model_dump())
        self.session.add(room)
        await self.session.commit()

    async def get_all(self) -> list[RoomOrm]:
        query = (
            select(RoomOrm)
            .options(selectinload(RoomOrm.players)
                .options(joinedload(PlayerOrm.card)
                    .options(joinedload(CardOrm.health)
                        .options(joinedload(HealthOrm.health_title))
                        .options(joinedload(HealthOrm.health_state)))
                    .options(joinedload(CardOrm.profession))
                    .options(joinedload(CardOrm.phobia))
                )
            )
        )
        result = await self.session.scalars(query)
        return result
