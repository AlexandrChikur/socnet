import databases
import sqlalchemy

from app.core.config import DATABASE_URL


database = databases.Database(str(DATABASE_URL))
engine = sqlalchemy.create_engine(str(DATABASE_URL))

