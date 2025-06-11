import random

Years = [1776, 1914, 1969, 2001, 2020]

# TODO: Step 1 - Return 'events.txt' for empty input, otherwise use the user-specified file.
def select_file(user_input):
    return user_input

# TODO: Step 2 - Read the file and handle FileNotFoundError, returning an empty string on error.
def read_events(file_name):
    return ""

# TODO: Step 3 - Randomly select a year from the Years list.
def select_random_year(years):
    return 0

# TODO: Step 4 - Find the event for the selected year. Return "Event/year not found." if not present.
def find_event(year, events):
    return "Event/year not found."

# TODO: Step 5 - Print the year and event in the format: "Year: Event Description"
def print_event(event, year):
    print("Event not implemented.")

if __name__ == "__main__":
    user_input = input("Enter event file [leave empty for events.txt]: ")
    event_file = select_file(user_input)
    events = read_events(event_file).split("\n")
    random_year = select_random_year(Years)
    if not random_year:
        print("No year selected.")
        quit()
    event = find_event(random_year, events)
    print_event(event, random_year)
