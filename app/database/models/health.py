from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.models.base import BaseOrm


class HealthTitleOrm(BaseOrm):
    __tablename__ = 'health_titles'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(unique=True)


class HealthStateOrm(BaseOrm):
    __tablename__ = 'health_states'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(unique=True)


class HealthOrm(BaseOrm):
    __tablename__ = 'health'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    health_title_id: Mapped[int] = mapped_column(ForeignKey('health_titles.id'))
    health_state_id: Mapped[int] = mapped_column(ForeignKey('health_states.id'))
    health_title: Mapped['HealthTitleOrm'] = relationship()
    health_state: Mapped['HealthStateOrm'] = relationship()
