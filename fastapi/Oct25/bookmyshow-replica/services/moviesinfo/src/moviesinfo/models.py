from sqlalchemy import String, Integer, Float, Text, Date, Enum, func
from sqlalchemy.orm import Mapped, mapped_column
from datetime import date
from moviesinfo.db import Base
import enum


class GenreEnum(str, enum.Enum):
    ACTION = "Action"
    DRAMA = "Drama"
    COMEDY = "Comedy"
    HORROR = "Horror"
    ROMANCE = "Romance"
    SCIFI = "Sci-Fi"
    THRILLER = "Thriller"
    ANIMATION = "Animation"
    DOCUMENTARY = "Documentary"


class Movie(Base):
    __tablename__ = "movies"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(200), nullable=False, index=True)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    genre: Mapped[GenreEnum] = mapped_column(Enum(GenreEnum), nullable=False)
    rating: Mapped[float] = mapped_column(Float, default=0.0)  # IMDb-style rating
    duration_minutes: Mapped[int] = mapped_column(Integer, nullable=True)  # runtime
    description: Mapped[str] = mapped_column(Text, nullable=True)
    director: Mapped[str] = mapped_column(String(120), nullable=True)
    cast: Mapped[str] = mapped_column(Text, nullable=True)  # comma-separated actor list
    release_date: Mapped[date] = mapped_column(Date, nullable=True)
    language: Mapped[str] = mapped_column(String(50), default="English")
    country: Mapped[str] = mapped_column(String(100), default="USA")
    created_at: Mapped[date] = mapped_column(Date, server_default=func.current_date())

    def __repr__(self) -> str:
        return f"<Movie {self.title} ({self.year}) ⭐ {self.rating}>"
