import random

Artists = ["Bob Dylan", "Beyoncé", "The Beatles", "Adele", "Nirvana"]

# TODO: Step 1 - Return 'lyrics.txt' for empty input, otherwise create the user-specified file with a default lyric.
def get_file_name(user_input):
    return user_input

# TODO: Step 2 - Read the file and handle FileNotFoundError, printing an error message and returning an empty string.
def read_lyrics(file_name):
    return ""

# TODO: Step 3 - Randomly select an artist from the Artists list.
def select_random_artist(artists):
    return ""

# TODO: Step 4 - Find the lyric for the selected artist. Return "Artist/lyric not found." if not present.
def find_lyric(artist, lyrics):
    return "Artist/lyric not found."

# TODO: Step 5 - Print the artist and lyric in the format: "Artist: Lyric"
def print_lyric(lyric, artist):
    print("Lyric not implemented.")

if __name__ == "__main__":
    user_input = input("Enter lyric file [leave empty for lyrics.txt]: ")
    lyric_file = get_file_name(user_input)
    lyrics = read_lyrics(lyric_file).split("\n")
    random_artist = select_random_artist(Artists)
    if not random_artist:
        print("No artist selected.")
        quit()
    lyric = find_lyric(random_artist, lyrics)
    print_lyric(lyric, random_artist)
