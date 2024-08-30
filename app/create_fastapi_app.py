from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.models.dp_helper import db_helper


@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    yield
    # shutdown
    await db_helper.dispose()


def create_app() -> FastAPI:
    app = FastAPI(
        lifespan=lifespan,
    )
    return app
