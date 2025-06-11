import unittest
import os
from io import StringIO
from contextlib import redirect_stdout
from unittest.mock import patch
from hysterical_event_funder import select_file, read_events, select_random_year, find_event, print_event

class TestHistoricalEventFinder(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Create a temporary test file
        cls.test_file = "test_events.txt"
        with open(cls.test_file, "w") as f:
            f.write("1776 ~ American Declaration of Independence\n1969 ~ Moon Landing")

    @classmethod
    def tearDownClass(cls):
        # Clean up the test file
        if os.path.exists(cls.test_file):
            os.remove(cls.test_file)

    def test_select_file_empty_input(self):
        self.assertEqual(select_file(""), "events.txt")

    def test_select_file_non_empty_input(self):
        self.assertEqual(select_file("custom.txt"), "custom.txt")

    def test_read_events_existing_file(self):
        content = read_events(self.test_file)
        self.assertIn("1776 ~ American Declaration of Independence", content)

    def test_read_events_non_existing_file(self):
        content = read_events("non_existent.txt")
        self.assertEqual(content, "")

    def test_select_random_year(self):
        with patch("random.choice", return_value=1776):
            self.assertEqual(select_random_year([1776, 1969]), 1776)

    def test_find_event_existing_year(self):
        events = ["1776 ~ American Declaration of Independence", "1969 ~ Moon Landing"]
        self.assertEqual(find_event(1776, events), "1776 ~ American Declaration of Independence")

    def test_find_event_non_existing_year(self):
        events = ["1776 ~ American Declaration of Independence"]
        self.assertEqual(find_event(2001, events), "Event/year not found.")

    def test_print_event(self):
        with StringIO() as buf, redirect_stdout(buf):
            print_event("1776 ~ American Declaration of Independence", 1776)
            output = buf.getvalue().strip()
        self.assertEqual(output, "Year: 1776 ~ American Declaration of Independence")

if __name__ == "__main__":
    unittest.main()
