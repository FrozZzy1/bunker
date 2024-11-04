from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from datetime import datetime


class BaseOrm(DeclarativeBase):
    created_at: Mapped[datetime] = mapped_column(
        default=datetime.utcnow(),
    )
    updated_at: Mapped[datetime] = mapped_column(
        default=datetime.utcnow(),
        onupdate=datetime.now(),
    )
