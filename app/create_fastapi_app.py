from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.exception_container import exception_container
from app.models.dp_helper import db_helper
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from app.sheduler_task.sheduler_task import set_actual_currency_rate_to_db
from fastapi.middleware.cors import CORSMiddleware


@asynccontextmanager
async def lifespan(app: FastAPI):
    task_scheduler = AsyncIOScheduler()
    task_scheduler.scheduled_job(
        set_actual_currency_rate_to_db,
        "cron",
        hour=10,
        minute=0,
        second=0,
        timezone="UTC",
    )
    yield
    # shutdown
    await db_helper.dispose()


def create_app() -> FastAPI:
    app = FastAPI(
        lifespan=lifespan,
    )
    origins = [
        "http://localhost",
        "http://localhost:8080",
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app = exception_container(app)

    return app
