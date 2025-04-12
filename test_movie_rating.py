import unittest
from domain.value_objects.MovieRating import MovieRating

class TestMovieRating(unittest.TestCase):

    def test_valid_movie_rating(self):
        """Test creating a valid MovieRating object."""
        rating = MovieRating(score=4.5, reviewer="John Doe")
        self.assertEqual(rating.score, 4.5)
        self.assertEqual(rating.reviewer, "John Doe")

    def test_invalid_score(self):
        """Test creating a MovieRating object with an invalid score."""
        with self.assertRaises(ValueError) as context:
            MovieRating(score=6.0, reviewer="John Doe")
        self.assertEqual(str(context.exception), "Score must be between 0.0 and 5.0")

    def test_invalid_reviewer(self):
        """Test creating a MovieRating object with an invalid reviewer."""
        with self.assertRaises(ValueError) as context:
            MovieRating(score=4.5, reviewer="")
        self.assertEqual(str(context.exception), "Reviewer must be a non-empty string")

    def test_eq(self):
        """Test that two MovieRating are the same if values are the same"""
        score = 4.5
        reviewer = "John"
        rating1 = MovieRating(score, reviewer)
        rating2 = MovieRating(score, reviewer)
        self.assertEqual(rating1, rating2)

    def test_ne(self):
        """Test that two MovieRating are not the same if values are different"""
        rating1 = MovieRating(4.5, "John")
        rating2 = MovieRating(4.500000001, "John")
        self.assertNotEqual(rating1, rating2)

if __name__ == "__main__":
    unittest.main()