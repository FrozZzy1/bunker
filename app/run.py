from fastapi import FastAPI, APIRouter
from contextlib import asynccontextmanager

from app.api.handlers.user import users_router
from app.api.handlers.room import rooms_router
from app.api.handlers.profession import professions_router
from app.api.handlers.card import cards_router
from app.api.handlers.player import players_router
from app.api.handlers.health import health_router
from app.api.handlers.health_state import health_states_router
from app.api.handlers.health_title import health_titles_router
from app.api.handlers.phobia import phobias_router
from app.api.handlers.baggage import baggages_router
from app.database.database import create_tables, delete_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    # await delete_tables()
    await create_tables()
    yield


def setup_handlers(*args) -> None:
    main_router = APIRouter(
        prefix='/api/v1/bunker',
    )
    for router in args:
        main_router.include_router(router)

    return main_router


app = FastAPI(
    title='bunker',
    lifespan=lifespan,
)
app.include_router(
    setup_handlers(
        users_router,
        rooms_router,
        professions_router,
        cards_router,
        players_router,
        health_router,
        health_states_router,
        health_titles_router,
        phobias_router,
        baggages_router,
    )
)
