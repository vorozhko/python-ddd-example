from sqlmodel import Session, select
from movies.entities.Movie import Movie
from typing import List, Optional

class MovieRepository:
    def __init__(self, session: Session):
        self.session = session

    def add_movie(self, movie: Movie):
        """Add a new movie to the database."""
        self.session.add(movie)
        self.session.commit()

    def get_movie_by_id(self, movie_id: str) -> Optional[Movie]:
        """Retrieve a movie by its ID."""
        movie = self.session.get(Movie, movie_id)
        if movie:
            return movie
        return None

    def get_all_movies(self) -> List[Movie]:
        """Retrieve all movies from the database."""
        statement = select(Movie)
        movies = self.session.exec(statement).all()
        return movies

    def delete_movie(self, movie_id: str):
        """Delete a movie by its ID."""
        movie = self.session.get(Movie, movie_id)
        if movie:
            self.session.delete(movie)
            self.session.commit()

    def update_movie(self, movie: Movie):
        """Update an existing movie."""
        self.session.add(movie)
        self.session.commit()