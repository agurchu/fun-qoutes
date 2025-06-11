import random

Movies = ["The Godfather", "Star Wars", "The Matrix", "Titanic", "Inception"]

# TODO: Step 1 - Return 'movies.txt' if input is empty, otherwise create and use the user-specified file.
def choose_file(user_input):
    if user_input == "":
        return "movies.txt"
    else:
        with open(user_input, "w") as f:
            f.write("Inception ~ Dreams steal your secrets.")
    return user_input

# TODO: Step 2 - Read the file and handle FileNotFoundError, returning an empty string if the file doesn't exist.
def read_movies(file_name):
    try:
        with open(file_name, "r") as f:
            return f.read()
    except:
        return ""

# TODO: Step 3 - Randomly select a movie from the Movies list.
def select_random_movie(movies):
    return ""

# TODO: Step 4 - Find the quote for the selected movie. Return "Movie/quote not found." if not present.
def find_quote(movie, quotes):
    return ""

# TODO: Step 5 - Print the movie and its quote in the format: "Movie: Quote"
def display_quote(quote, movie):
    print("Quote not implemented.")

if __name__ == "__main__":
    user_input = input("Enter movie file [leave empty for movies.txt]: ")
    movie_file = choose_file(user_input)
    quotes = read_movies(movie_file).split("\n")
    random_movie = select_random_movie(Movies)
    if not random_movie:
        print("No movie selected.")
        quit()
    quote = find_quote(random_movie, quotes)
    display_quote(quote, random_movie)
