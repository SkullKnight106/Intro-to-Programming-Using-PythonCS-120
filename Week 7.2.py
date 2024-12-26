# Week 7.2
# Write a program that opens a specified text file then displays a list of all the unique words found in the file.
# Hint: Store each word as an element of a set.
# Use read function from file input/output functions.


def extract_unique_words(filepath):
    """
    Reads a text file and extracts all unique words.
    :param filepath: The path to the file
    :return: A set of unique words
    """
    try:
        with open(filepath, 'r') as file:
            content = file.read()
            # Split the content into words and clean them
            words = content.split()
            # Use a set to store unique words (ignoring case)
            unique_words = {word.strip('.,!?;:"()[]').lower() for word in words}
            return unique_words
    except FileNotFoundError:
        print("Error: File not found.")
        return set()

def main():
    filepath = r"C:\Users\Bredy\OneDrive\Documents\Capitol Technology University\Intro to Programming Using PythonCS-120\specified.txt"

    # Step 1: Extract unique words from the file
    unique_words = extract_unique_words(filepath)

    # Step 2: Display the unique words
    if unique_words:
        print("\nUnique words found in the file:")
        for word in sorted(unique_words):  # Sort alphabetically for readability
            print(word)

# Execute the program
main()
