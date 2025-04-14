import unittest
from movies.entities.Movie import Movie
from movies.value_objects.MovieRating import MovieRating

class TestMovieEntity(unittest.TestCase):

    def test_create_movie_with_no_title(self):
        """Test for empty title"""        
        movie = Movie(title="")
        self.assertEqual(movie.title, "")
        
    def test_create_movie(self):
        """Test creating a Movie entity with a title."""
        movie = Movie(title="Inception")
        self.assertEqual(movie.title, "Inception")
        self.assertEqual(len(movie.ratings), 0)  # No ratings initially
        self.assertIsNotNone(movie.id)  # Ensure the ID is generated

    def test_add_rating(self):
        """Test adding a valid MovieRating to a Movie."""
        movie = Movie(title="Inception")
        rating = MovieRating(score=4.5, reviewer="John Doe")
        movie.add_rating(rating)
        self.assertEqual(len(movie.ratings), 1)
        self.assertEqual(movie.ratings[0], rating)

    def test_add_invalid_rating(self):
        """Test adding an invalid rating raises a ValueError."""
        movie = Movie(title="Inception")
        with self.assertRaises(ValueError) as context:
            movie.add_rating("Invalid Rating")  # Not a MovieRating object
        self.assertEqual(str(context.exception), "Invalid rating. Must be a MovieRating object.")

    def test_average_rating(self):
        """Test calculating the average rating of a Movie."""
        movie = Movie(title="Inception")
        movie.add_rating(MovieRating(score=4.0, reviewer="John Doe"))
        movie.add_rating(MovieRating(score=5.0, reviewer="Jane Smith"))
        self.assertEqual(movie.average_rating(), 4.5)  # Average of 4.0 and 5.0

    def test_average_rating_no_ratings(self):
        """Test average rating when no ratings are present."""
        movie = Movie(title="Inception")
        self.assertEqual(movie.average_rating(), 0.0)  # No ratings, average is 0.0

    def test_set_update_geners(self):
        movieGenres = ['Sci-Fi', 'Cyberpunk', 'AI']
        movie = Movie(title="Matrix", genres=movieGenres)
        self.assertEqual(movie.genres, movieGenres)
        movie.genres.remove('AI')
        self.assertTrue('AI' not in movie.genres)


if __name__ == "__main__":
    unittest.main()