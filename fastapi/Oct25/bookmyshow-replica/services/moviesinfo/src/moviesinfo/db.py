"""In this module we will be creating necessary
functions, classes to deal with postgres database 
async
"""

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')

# Async engine
engine = create_async_engine(DATABASE_URL, echo=True)

# Session factory (2.0 style)
async_session = async_sessionmaker(engine, expire_on_commit=False)

# Declarative base (new 2.0 API)
class Base(DeclarativeBase):
    pass
