"""Movie class manages rating list"""

from dataclasses import dataclass, field
from typing import List
from uuid import uuid4
from movies.value_objects.MovieRating import MovieRating

@dataclass
class Movie:
    title: str
    id: str = field(default_factory=lambda: str(uuid4()))
    ratings: List[MovieRating] = field(default_factory=list)

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