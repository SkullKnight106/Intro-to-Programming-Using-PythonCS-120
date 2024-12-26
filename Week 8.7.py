# Week 8.7
# Write a program that reads the contents of a text file. The program should create a dictionary in which the key-value pairs are described as follows: 
# Key. The keys are the individual words found in the file. 
# Values. Each value is a list that contains the line numbers in the file where the word (the key) is found. 
# For example, suppose the word “robot” is found in lines 7, 18, 94, and 138. 
# The dictionary would contain an element in which the key was the string “robot”, and the value was a list containing the numbers 7, 18, 94, and 138. 
# Once the dictionary is built, the program should create another text file, known as a word index, listing the contents of the dictionary. 
# The word index file should contain an alphabetical listing of the words that are stored as keys in the dictionary, along with the line numbers where the words appear in the original file. 
# The image below shows an example of an original text file (Kennedy.txt) and its index file (index.txt).


def create_word_index(input_file, output_file):
    """
    Reads the contents of a text file, creates a dictionary where keys are
    words and values are lists of line numbers where the word appears, and
    writes the word index to another file.
    """
    word_dict = {}

    # Read the input file line by line
    with open(input_file, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            # Split the line into words
            words = line.strip().split()
            for word in words:
                # Remove punctuation and convert to lowercase
                cleaned_word = ''.join(char for char in word if char.isalnum()).lower()
                if cleaned_word:  # Skip empty strings
                    if cleaned_word not in word_dict:
                        word_dict[cleaned_word] = []
                    word_dict[cleaned_word].append(line_number)

    # Write the word index to the output file
    with open(output_file, 'w') as file:
        for word in sorted(word_dict):
            line_numbers = ', '.join(map(str, word_dict[word]))
            file.write(f"{word}: {line_numbers}\n")


# Specify the input and output file names
input_filename = "input.txt"  # Change this to your input file's name
output_filename = "word_index.txt"  # Name of the output file

# Create the word index
create_word_index(input_filename, output_filename)

print(f"Word index has been created in the file '{output_filename}'.")

