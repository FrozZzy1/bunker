from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.models.base import BaseOrm


class CardOrm(BaseOrm):
    __tablename__ = 'cards'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    player: Mapped['PlayerOrm'] = relationship()
    profession_id: Mapped[int] = mapped_column(ForeignKey('professions.id'))
    phobia_id: Mapped[int] = mapped_column(ForeignKey('phobias.id'))
    health_id: Mapped[int] = mapped_column(ForeignKey('health.id'))
    baggage_id: Mapped[int] = mapped_column(ForeignKey('baggages.id'))

    profession: Mapped['ProfessionOrm'] = relationship()
    phobia: Mapped['PhobiaOrm'] = relationship()
    health: Mapped['HealthOrm'] = relationship()
    baggage: Mapped['BaggageOrm'] = relationship()
