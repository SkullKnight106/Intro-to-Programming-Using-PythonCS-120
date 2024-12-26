# Week 8.6
# Write a program with a function that accepts a string as an argument and returns a copy of the string with the first character of each sentence capitalized. 
# For instance, if the argument is “hello. my name is Joe. what is your name?” the function should return the string “Hello. My name is Joe. What is your name?” 
# The program should let the user enter a string and then pass it to the function. The modified string should be displayed. 

def capitalize_sentences(input_string):
    """
    Capitalizes the first character of each sentence in the given string.
    """
    # Split the string into sentences
    sentences = input_string.split('. ')
    # Capitalize the first character of each sentence and join them back
    capitalized_sentences = '. '.join(sentence.capitalize() for sentence in sentences)
    return capitalized_sentences


def main():
    """
    Main function to collect user input, process it, and display the result.
    """
    # Get input from the user
    user_input = input("Enter a string with multiple sentences: ").strip()
    
    # Call the capitalize_sentences function
    modified_string = capitalize_sentences(user_input)
    
    # Display the modified string
    print("\nModified String:")
    print(modified_string)


# Execute the program
main()


