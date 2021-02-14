from typing import Callable

from fastapi import FastAPI


def create_startup_eventhandler(app: FastAPI) -> Callable:
    async def start_app() -> None:
        pass

    return start_app


def create_shutdown_eventhandler(app: FastAPI) -> Callable:
    async def stop_app() -> None:
        pass

    return stop_app
