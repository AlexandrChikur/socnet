from typing import Callable

from app.db.events import db_connect, db_disconnect
from fastapi import FastAPI


def create_startup_eventhandler(app: FastAPI) -> Callable:
    async def start_app() -> None:
        await db_connect()

    return start_app


def create_shutdown_eventhandler(app: FastAPI) -> Callable:
    async def stop_app() -> None:
        await db_disconnect()

    return stop_app
