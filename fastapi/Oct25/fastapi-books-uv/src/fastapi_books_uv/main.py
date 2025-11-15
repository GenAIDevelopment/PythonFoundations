import os
from contextlib import asynccontextmanager
from typing import Annotated, AsyncGenerator

from fastapi import Depends, FastAPI, HTTPException, status
from pydantic import BaseModel
from sqlalchemy import Integer, String, select
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


# ============================================================
# Database configuration
# ============================================================

# In Docker compose we pass:
#   postgresql+asyncpg://postgres:postgres@db:5432/books_db
# For local dev you can run Postgres locally on localhost:5432.
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+asyncpg://postgres:postgres@localhost:5432/books_db",
)


class Base(DeclarativeBase):
    """Base class for SQLAlchemy models."""
    pass


class Book(Base):
    """SQLAlchemy model for the 'books' table."""
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(200))
    author: Mapped[str] = mapped_column(String(120))
    pages: Mapped[int] = mapped_column(Integer)
    description: Mapped[str | None] = mapped_column(String(500), nullable=True)


# Async SQLAlchemy engine and session factory
engine = create_async_engine(DATABASE_URL, echo=True)
AsyncSessionLocal = async_sessionmaker(engine, expire_on_commit=False)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    """FastAPI dependency that provides an async DB session."""
    async with AsyncSessionLocal() as session:
        yield session


# ============================================================
# Pydantic schemas
# ============================================================

class BookCreate(BaseModel):
    title: str
    author: str
    pages: int
    description: str | None = None


class BookRead(BookCreate):
    id: int

    class Config:
        orm_mode = True  # works with FastAPI to read from ORM objects


class BookUpdate(BaseModel):
    title: str | None = None
    author: str | None = None
    pages: int | None = None
    description: str | None = None


# ============================================================
# FastAPI app + lifespan (startup/shutdown)
# ============================================================

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Lifespan handler runs on startup and shutdown.

    Here we auto-create tables on startup (for demo).
    In real projects, prefer Alembic migrations.
    """
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    # (No special shutdown logic needed here)


app = FastAPI(
    title="Books API (FastAPI + Async SQLAlchemy + Postgres)",
    lifespan=lifespan,
)


# ============================================================
# CRUD endpoints
# ============================================================

# Create
@app.post("/books", response_model=BookRead, status_code=status.HTTP_201_CREATED)
async def create_book(
    book: BookCreate,
    session: Annotated[AsyncSession, Depends(get_session)],
):
    db_book = Book(**book.dict())
    session.add(db_book)
    await session.commit()
    await session.refresh(db_book)
    return db_book


# Read all
@app.get("/books", response_model=list[BookRead])
async def list_books(
    session: Annotated[AsyncSession, Depends(get_session)],
):
    result = await session.execute(select(Book))
    books = result.scalars().all()
    return books


# Read one
@app.get("/books/{book_id}", response_model=BookRead)
async def get_book(
    book_id: int,
    session: Annotated[AsyncSession, Depends(get_session)],
):
    result = await session.execute(select(Book).where(Book.id == book_id))
    db_book = result.scalar_one_or_none()
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book


# Update (partial)
@app.patch("/books/{book_id}", response_model=BookRead)
async def update_book(
    book_id: int,
    book: BookUpdate,
    session: Annotated[AsyncSession, Depends(get_session)],
):
    result = await session.execute(select(Book).where(Book.id == book_id))
    db_book = result.scalar_one_or_none()
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")

    update_data = book.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_book, field, value)

    await session.commit()
    await session.refresh(db_book)
    return db_book


# Delete
@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(
    book_id: int,
    session: Annotated[AsyncSession, Depends(get_session)],
):
    result = await session.execute(select(Book).where(Book.id == book_id))
    db_book = result.scalar_one_or_none()
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")

    await session.delete(db_book)
    await session.commit()
    return None
