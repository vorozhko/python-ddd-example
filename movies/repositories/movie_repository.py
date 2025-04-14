from sqlmodel import Session, select
from movies.entities.Movie import Movie
from movies.mappers.movie_mapper import MovieMapper, MovieTable
from typing import List, Optional

class MovieRepository:
    def __init__(self, session: Session):
        self.session = session

    def add_movie(self, movie: Movie):
        """Add a new movie to the database."""
        movie_table = MovieMapper.to_table(movie)
        self.session.add(movie_table)
        self.session.commit()

    def get_movie_by_id(self, movie_id: str) -> Optional[Movie]:
        """Retrieve a movie by its ID."""
        movie_table = self.session.get(MovieTable, movie_id)
        if movie_table:
            return MovieMapper.to_domain(movie_table)
        return None

    def get_all_movies(self) -> List[Movie]:
        """Retrieve all movies from the database."""
        statement = select(MovieTable)
        movie_tables = self.session.exec(statement).all()
        return [MovieMapper.to_domain(mt) for mt in movie_tables]

    def delete_movie(self, movie_id: str):
        """Delete a movie by its ID."""
        movie_table = self.session.get(MovieTable, movie_id)
        if movie_table:
            self.session.delete(movie_table)
            self.session.commit()

    def update_movie(self, movie: Movie):
        """Update an existing movie."""
        movie_table = MovieMapper.to_table(movie)
        self.session.add(movie_table)
        self.session.commit()