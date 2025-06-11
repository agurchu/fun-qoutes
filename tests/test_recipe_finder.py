import unittest
import os
from io import StringIO
from contextlib import redirect_stdout
from unittest.mock import patch
from recipe_finder import choose_file, read_recipes, select_random_dish, find_ingredient, print_ingredient

class TestRecipeIngredientFinderNew(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Create temporary test file
        cls.test_file = "test_recipes_new.txt"
        with open(cls.test_file, "w") as f:
            f.write("Pizza ~ Cheese\n\n")

    @classmethod
    def tearDownClass(cls):
        # Clean up test file
        if os.path.exists(cls.test_file):
            os.remove(cls.test_file)

    def test_choose_file_non_text_extension(self):
        self.assertEqual(choose_file("recipes.pdf"), "recipes.pdf")

    def test_read_recipes_trailing_newlines(self):
        content = read_recipes(self.test_file)
        self.assertIn("Pizza ~ Cheese", content)

    def test_select_random_dish_duplicates(self):
        with patch("random.choice", return_value="Pizza"):
            self.assertEqual(select_random_dish(["Pizza", "Pizza"]), "Pizza")

    def test_find_ingredient_empty_list(self):
        self.assertEqual(find_ingredient("Pizza", []), "Dish/ingredient not found.")

    def test_print_ingredient_long_name(self):
        ingredient = "Pizza ~ " + "Ingredient " * 20
        with StringIO() as buf, redirect_stdout(buf):
            print_ingredient(ingredient, "Pizza")
            output = buf.getvalue().strip()
        self.assertIn("Dish: Pizza ~ Ingredient", output)

if __name__ == "__main__":
    unittest.main()
