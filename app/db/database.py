import databases
import sqlalchemy

from app.core.config import get_settings


DATABASE_URL = get_settings().database_url
database = databases.Database(DATABASE_URL)
engine = sqlalchemy.create_engine(DATABASE_URL)

