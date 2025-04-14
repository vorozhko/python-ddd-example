from movies.value_objects.MovieRating import MovieRating
from movies.database import init_db, get_session
from movies.entities.Movie import Movie
from movies.repositories.movie_repository import MovieRepository
from sqlmodel import Session

def main():
    # Initialize the database
    init_db()

    # Create a new movie
    movie = Movie(
        title="Inception",
        genres=["Sci-Fi", "Thriller"],
         ratings=[MovieRating(score=4.5, reviewer="John Doe")],
        release_date="2010-07-16",
        duration=148
    )

    session = get_session()
    repo = MovieRepository(session)
    repo.add_movie(movie)

    # Retrieve and print all movies
    movies = repo.get_all_movies()
    for m in movies:
        print(m)

if __name__ == "__main__":
    main()