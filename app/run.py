from fastapi import FastAPI, APIRouter

app = FastAPI(
    title='bunker',
)

router = APIRouter(
    prefix='/api/v1/bunker',
)


app.include_router(router)
