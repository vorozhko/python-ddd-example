from movies.value_objects.MovieRating import MovieRating
from movies.entities.Movie import Movie
from movies.mappers.movie_table import MovieTable


class MovieMapper:
    @staticmethod
    def to_table(movie: Movie) -> MovieTable:
        """Converts a Movie domain model to a MovieTable database model."""
        return MovieTable(
            id=movie.id,
            title=movie.title,
            genres=movie.genres,
            ratings=[{"score": r.score, "reviewer": r.reviewer} for r in movie.ratings],
            duration=movie.duration,
            release_date=movie.release_date,
        )

    @staticmethod
    def to_domain(movie_table: MovieTable) -> Movie:
        """Converts a MovieTable database model to a Movie domain model."""
        return Movie(
            id=movie_table.id,
            title=movie_table.title,
            genres=movie_table.genres,
            ratings=[
                MovieRating(score=r["score"], reviewer=r["reviewer"])
                for r in movie_table.ratings
            ],
            duration=movie_table.duration,
            release_date=movie_table.release_date,
        )