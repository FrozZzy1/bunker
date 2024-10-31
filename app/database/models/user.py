from sqlalchemy.orm import Mapped, mapped_column

from app.database.models.base import BaseOrm


class UserOrm(BaseOrm):
    __tablename__ = 'users'

    tg_id: Mapped[str] = mapped_column(unique=True)
    tg_username: Mapped[str] = mapped_column(unique=True)
    name: Mapped[str]
