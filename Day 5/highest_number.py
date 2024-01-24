# Take input from the user
user_input = input("Enter numbers separated by spaces: ")

# Convert the input string into a list of integers
numbers = [int(x) for x in user_input.split()]

if not numbers:
    print("The list is empty.")
else:
    highest = numbers[0]

    for num in numbers:
        if num > highest:
            highest = num

    print(f"The highest number is: {highest}")
