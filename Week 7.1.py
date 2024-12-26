# Week 7.1
# Copy and paste one of your previous homework step-by-step breakdowns into a file. Read the data in from the file and store it in a list. 
# Next, allow the user to enter a word that will be stored as a string. Search the list for this string. If this string is found, return its location in the list. 
# If not, inform the user that the string does not exist in the list. Use string slicing to search for only a section of the inputted string. 
# Experiment with this; see how altering the string causes more or less matches to occur. 

def read_file_to_list(filepath):
    """
    Reads the contents of the file and stores each line in a list.
    :param filepath: The full path to the file
    :return: A list containing the lines of the file
    """
    try:
        with open(filepath, 'r') as file:
            lines = file.readlines()
            return [line.strip() for line in lines]  # Remove leading/trailing whitespace
    except FileNotFoundError:
        print("Error: File not found.")
        return []

def search_string_in_list(data_list, search_string):
    """
    Searches for a string in a list and returns its location or informs the user if not found.
    :param data_list: The list to search
    :param search_string: The string to search for
    """
    for index, line in enumerate(data_list):
        if search_string in line:
            print(f"Exact match found at index {index}: {line}")
            return
    print("The string does not exist in the list.")

def search_partial_string_in_list(data_list, partial_string):
    """
    Searches for partial matches of a string in a list.
    :param data_list: The list to search
    :param partial_string: The substring to search for
    """
    print("\nSearching for partial matches...")
    matches_found = False
    for index, line in enumerate(data_list):
        if partial_string in line:
            print(f"Partial match found at index {index}: {line}")
            matches_found = True
    if not matches_found:
        print("No partial matches found.")

def main():
    filepath = r"C:\Users\Bredy\OneDrive\Documents\Capitol Technology University\Intro to Programming Using PythonCS-120\step-by-step breakdowns.txt"

    # Read file and store in a list
    data_list = read_file_to_list(filepath)
    if not data_list:  # Exit if the file could not be read
        return

    # Prompt the user to enter a word
    search_string = input("Enter the word to search for: ")

    # Search for the exact string
    search_string_in_list(data_list, search_string)

    # Use string slicing to search for a partial match
    slice_length = min(len(search_string), 3)  # Define how much to slice for partial search
    partial_string = search_string[:slice_length]
    search_partial_string_in_list(data_list, partial_string)

# Execute the program
main()


