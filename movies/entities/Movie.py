"""Movie class manages rating list"""

from typing import List
from uuid import uuid4
from movies.value_objects.MovieRating import MovieRating
from sqlmodel import SQLModel, Field
from sqlalchemy import Column
from sqlalchemy.types import JSON


class Movie(SQLModel, table=True):
    title: str = Field(index=True)
    id: str = Field(default_factory=lambda: str(uuid4()), primary_key=True)
    genres: List[str] = Field(default_factory=list, sa_column=Column(JSON))  # Use Column(JSON)
    ratings: List[dict] = Field(default_factory=list, sa_column=Column(JSON))  # Use Column(JSON)
    duration: int = 0
    release_date: str | None = None

    def add_rating(self, rating: MovieRating):
        """Adds a new rating to the movie."""
        if not isinstance(rating, MovieRating):
            raise ValueError("Invalid rating. Must be a MovieRating object.")
        self.ratings.append(rating)

    def average_rating(self) -> float:
        """Calculates the average score of all ratings."""
        if not self.ratings:
            return 0.0
        return sum(rating.score for rating in self.ratings) / len(self.ratings)
    
    def __post_init__(self):
        if not self.title.isalpha():
            raise ValueError("Ttitle must have an alpha numberic value")
