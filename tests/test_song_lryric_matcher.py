import unittest
import os
from io import StringIO
from contextlib import redirect_stdout
from unittest.mock import patch
from song_lyric_matcher import get_file_name, read_lyrics, select_random_artist, find_lyric, print_lyric

class TestSongLyricMatcher(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Create a temporary test file
        cls.test_file = "test_lyrics.txt"
        with open(cls.test_file, "w") as f:
            f.write("Bob Dylan ~ Like a Rolling Stone\nThe Beatles ~ Let It Be")

    @classmethod
    def tearDownClass(cls):
        # Clean up the test file
        if os.path.exists(cls.test_file):
            os.remove(cls.test_file)
        if os.path.exists("custom_lyrics.txt"):
            os.remove("custom_lyrics.txt")

    def test_get_file_name_empty_input(self):
        self.assertEqual(get_file_name(""), "lyrics.txt")

    def test_get_file_name_non_empty_input(self):
        result = get_file_name("custom_lyrics.txt")
        self.assertEqual(result, "custom_lyrics.txt")
        self.assertTrue(os.path.exists("custom_lyrics.txt"))

    def test_read_lyrics_existing_file(self):
        content = read_lyrics(self.test_file)
        self.assertIn("Bob Dylan ~ Like a Rolling Stone", content)

    def test_read_lyrics_non_existing_file(self):
        content = read_lyrics("non_existent.txt")
        self.assertEqual(content, "")

    def test_select_random_artist(self):
        with patch("random.choice", return_value="Bob Dylan"):
            self.assertEqual(select_random_artist(["Bob Dylan", "The Beatles"]), "Bob Dylan")

    def test_find_lyric_existing_artist(self):
        lyrics = ["Bob Dylan ~ Like a Rolling Stone", "The Beatles ~ Let It Be"]
        self.assertEqual(find_lyric("Bob Dylan", lyrics), "Bob Dylan ~ Like a Rolling Stone")

    def test_find_lyric_non_existing_artist(self):
        lyrics = ["Bob Dylan ~ Like a Rolling Stone"]
        self.assertEqual(find_lyric("Adele", lyrics), "Artist/lyric not found.")

    def test_print_lyric(self):
        with StringIO() as buf, redirect_stdout(buf):
            print_lyric("Bob...

Something went wrong, please refresh to reconnect or try again.
