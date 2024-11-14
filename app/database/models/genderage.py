from sqlalchemy.orm import Mapped, mapped_column

from app.database.models.base import BaseOrm


class GenderageOrm(BaseOrm):
    __tablename__ = 'genderages'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    gender: Mapped[str] = mapped_column(default='мужской')
    age: Mapped[int]
