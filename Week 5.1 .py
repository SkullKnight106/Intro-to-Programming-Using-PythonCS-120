# Week 5.1
# Assume a file containing a series of integers is named numbers.txt and exists on the computer’s disk. 
# Write a program that reads all of the numbers stored in the file and calculates their total.

def calculate_total_from_file(filename):
    try:
        # Open the file in read mode
        with open(filename, 'r') as file:
            total = 0
            # Read each line, convert to integer, and add to the total
            for line in file:
                total += int(line.strip())
        print(f"The total of the numbers in {filename} is: {total}")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except ValueError:
        print("Error: The file contains a non-integer value.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Call the function with the filename
calculate_total_from_file('C:\\Users\\Bredy\\OneDrive\\Documents\\Capitol Technology University\\Intro to Programming Using PythonCS-120\\numbers.txt')

