from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.models.base import BaseOrm


class PlayerOrm(BaseOrm):
    __tablename__ = 'players'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    card_id: Mapped[int] = mapped_column(ForeignKey('cards.id'), nullable=True)
    # card: Mapped['CardOrm'] = relationship()
    room_id: Mapped[int] = mapped_column(ForeignKey('rooms.id'))
