"""MovieRating class contains a movie rating"""

from dataclasses import dataclass

@dataclass(frozen=True)
class MovieRating:
    score: float
    reviewer: str

    def __post_init__(self):
        if not (0.0 <= self.score <= 5.0):
            raise ValueError("Score must be between 0.0 and 5.0")
        if not self.reviewer or not isinstance(self.reviewer, str):
            raise ValueError("Reviewer must be a non-empty string")
        
    def __ne__(self, other):
        return not (self == other)
    