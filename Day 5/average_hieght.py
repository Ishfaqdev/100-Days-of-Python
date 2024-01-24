# Take input from the user for the list of heights
heights_str = input("Enter a list of heights separated by spaces: ")

# Convert the input string into a list of floats
heights = [float(height) for height in heights_str.split()]

# Check if the list is not empty
if not heights:
    print("The list of heights is empty.")
else:
    # Calculate the average height
    average_height = sum(heights) / len(heights)

    # Print the average height
    print(f"The average height is: {average_height}")
