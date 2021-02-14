from .database import database


async def db_connect() -> None:
    await database.connect()
    
async def db_disconnect() -> None:
    await database.disconnect()