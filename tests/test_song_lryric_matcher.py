import unittest
import os
from io import StringIO
from contextlib import redirect_stdout
from unittest.mock import patch
from song_lyric_matcher import get_file_name, read_lyrics, select_random_artist, find_lyric, print_lyric

class TestSongLyricMatcherNew(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Create temporary test file
        cls.test_file = "test_lyrics_new.txt"
        with open(cls.test_file, "w") as f:
            f.write("Bob Dylan ~ Like a Rolling Stone")

    @classmethod
    def tearDownClass(cls):
        # Clean up test files
        for file in [cls.test_file, "custom lyrics.txt"]:
            if os.path.exists(file):
                os.remove(file)

    def test_get_file_name_with_spaces(self):
        result = get_file_name("custom lyrics.txt")
        self.assertEqual(result, "custom lyrics.txt")
        self.assertTrue(os.path.exists("custom lyrics.txt"))

    def test_read_lyrics_single_line(self):
        content = read_lyrics(self.test_file)
        self.assertEqual(content, "Bob Dylan ~ Like a Rolling Stone")

    def test_select_random_artist_invalid_entry(self):
        with patch("random.choice", return_value=""):
            self.assertEqual(select_random_artist(["", "The Beatles"]), "")

    def test_find_lyric_missing_delimiter(self):
        lyrics = ["Bob Dylan Like a Rolling Stone", "The Beatles ~ Let It Be"]
        self.assertEqual(find_lyric("Bob Dylan", lyrics), "Artist/lyric not found.")

    def test_print_lyric_empty_lyric(self):
        with StringIO() as buf, redirect_stdout(buf):
            print_lyric("", "Bob Dylan")
            output = buf.getvalue().strip()
        self.assertEqual(output, "Artist: ")

if __name__ == "__main__":
    unittest.main()
