from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.models.base import BaseOrm


class CardOrm(BaseOrm):
    __tablename__ = 'cards'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    player: Mapped['PlayerOrm'] = relationship()
    profession_id: Mapped[int] = mapped_column(
        ForeignKey('professions.id'),
        unique=True,
    )
    profession: Mapped['ProfessionOrm'] = relationship()
