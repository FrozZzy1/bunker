from sqlalchemy.orm import Mapped, mapped_column

from app.database.models.base import BaseOrm


class PhysiqueOrm(BaseOrm):
    __tablename__ = 'physique'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(unique=True)
