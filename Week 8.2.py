# Week 8.2
# Design a program that prompts the user to enter the names of two primary colors to mix. 
# If the user enters anything other than “red,” “blue,” or “yellow,” the program should display an error message. 
# Otherwise, the program should display the name of the secondary color that results. 
# Integrate exception handling to provide the user with context when an exception occurs. 

def mix_colors(color1, color2): # A utility function that maps valid primary color combinations to their secondary colors using a dictionary. Returns the resulting secondary color or an error message.
    """
    Determines the resulting color from mixing two primary colors.
    :param color1: The first primary color
    :param color2: The second primary color
    :return: The secondary color or an error message if inputs are invalid
    """
    color_combinations = {   # This defines a dictionary called color_combinations to store mappings of two colors (input as tuples) to their resulting combination (a secondary color).
                                # The dictionary is designed to handle two input colors, regardless of their order.
        ('red', 'blue'): 'purple',  # The keys are tuples representing the combinations of two colors
        ('blue', 'red'): 'purple',
        ('red', 'yellow'): 'orange',
        ('yellow', 'red'): 'orange',
        ('blue', 'yellow'): 'green',
        ('yellow', 'blue'): 'green',
    }

    return color_combinations.get((color1, color2), "Error: Invalid color combination.") # This line looks up the result of mixing color1 and color2 in the color_combinations dictionary.
                                                                                            # .get(): A dictionary method that retrieves a value for a given key
def main():
    try:
        # Prompt the user to enter two primary colors
        color1 = input("Enter the first primary color (red, blue, yellow): ").strip().lower() # .strip(): Removes any leading/trailing spaces.
        color2 = input("Enter the second primary color (red, blue, yellow): ").strip().lower() # .lower(): Converts the input to lowercase to ensure consistency and avoid case sensitivity issues.

        # Validate user input
        valid_colors = {'red', 'blue', 'yellow'}
        if color1 not in valid_colors or color2 not in valid_colors:
            raise ValueError("Only 'red', 'blue', or 'yellow' are valid colors.") # If either input is invalid, a ValueError is raised with a clear message.

        # Display the resulting secondary color
        result = mix_colors(color1, color2)
        if "Error" in result:
            print(result)
        else:
            print(f"Mixing {color1} and {color2} results in {result}.")

    except ValueError as e:
        print(f"Input Error: {e}") # Handles invalid inputs by catching ValueError and displaying a user-friendly error message.
    except Exception as e:
        print(f"An unexpected error occurred: {e}") # Catches and handles any other unexpected errors to prevent the program from crashing.

# Execute the program
main()


