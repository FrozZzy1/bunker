from sqlalchemy.ext.asyncio import AsyncSession


class AbsRepo:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session