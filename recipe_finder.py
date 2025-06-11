import random

Dishes = ["Pizza", "Sushi", "Pasta", "Tacos", "Curry"]

# TODO: Step 1 - Return 'recipes.txt' for empty input, otherwise use the user-specified file.
def choose_file(user_input):
    return user_input

# TODO: Step 2 - Read the file and handle FileNotFoundError, returning an empty string on error.
def read_recipes(file_name):
    return ""

# TODO: Step 3 - Randomly select a dish from the Dishes list.
def select_random_dish(dishes):
    return ""

# TODO: Step 4 - Find the main ingredient for the selected dish. Return "Dish/ingredient not found." if not present.
def find_ingredient(dish, recipes):
    return "Dish/ingredient not found."

# TODO: Step 5 - Print the dish and ingredient in the format: "Dish: Main Ingredient"
def print_ingredient(ingredient, dish):
    print("Ingredient not implemented.")

if __name__ == "__main__":
    user_input = input("Enter recipe file [leave empty for recipes.txt]: ")
    recipe_file = choose_file(user_input)
    recipes = read_recipes(recipe_file).split("\n")
    random_dish = select_random_dish(Dishes)
    if not random_dish:
        print("No dish selected.")
        quit()
    ingredient = find_ingredient(random_dish, recipes)
    print_ingredient(ingredient, random_dish)
