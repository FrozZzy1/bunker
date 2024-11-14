from sqlalchemy.orm import Mapped, mapped_column

from app.database.models.base import BaseOrm


class TraitOrm(BaseOrm):
    __tablename__ = 'traits'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(unique=True)
