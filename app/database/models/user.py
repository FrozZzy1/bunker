from sqlalchemy.orm import Mapped, mapped_column

from app.database.models.base import BaseOrm


class UserOrm(BaseOrm):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    tg_id: Mapped[int] = mapped_column(unique=True)
    name: Mapped[str]
