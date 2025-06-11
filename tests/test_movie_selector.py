import unittest
import os
from io import StringIO
from contextlib import redirect_stdout
from unittest.mock import patch
from movie_quote_selector import choose_file, read_movies, select_random_movie, find_quote, display_quote

class TestMovieQuoteSelector(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Create a temporary test file
        cls.test_file = "test_movies.txt"
        with open(cls.test_file, "w") as f:
            f.write("The Godfather ~ Leave the gun, take the cannoli.\nStar Wars ~ May the Force be with you.")

    @classmethod
    def tearDownClass(cls):
        # Clean up the test file
        if os.path.exists(cls.test_file):
            os.remove(cls.test_file)
        if os.path.exists("custom_movies.txt"):
            os.remove("custom_movies.txt")

    def test_choose_file_empty_input(self):
        self.assertEqual(choose_file(""), "movies.txt")

    def test_choose_file_non_empty_input(self):
        result = choose_file("custom_movies.txt")
        self.assertEqual(result, "custom_movies.txt")
        self.assertTrue(os.path.exists("custom_movies.txt"))

    def test_read_movies_existing_file(self):
        content = read_movies(self.test_file)
        self.assertIn("The Godfather ~ Leave the gun, take the cannoli.", content)

    def test_read_movies_non_existing_file(self):
        content = read_movies("non_existent.txt")
        self.assertEqual(content, "")

    def test_select_random_movie(self):
        with patch("random.choice", return_value="Star Wars"):
            self.assertEqual(select_random_movie(["The Godfather", "Star Wars"]), "Star Wars")

    def test_find_quote_existing_movie(self):
        quotes = ["The Godfather ~ Leave the gun, take the cannoli.", "Star Wars ~ May the Force be with you."]
        self.assertEqual(find_quote("Star Wars", quotes), "Star Wars ~ May the Force be with you.")

    def test_find_quote_non_existing_movie(self):
        quotes = ["The Godfather ~ Leave the gun, take the cannoli."]
        self.assertEqual(find_quote("Titanic", quotes), "Movie/quote not found.")

    def test_display_quote(self):
        with StringIO() as buf, redirect_stdout(buf):
            display_quote("Star Wars ~ May the Force be with you.", "Star Wars")
            output = buf.getvalue().strip()
        self.assertEqual(output, "Movie: Star Wars ~ May the Force be with you.")

if __name__ == "__main__":
    unittest.main()
