# datatype exercise

two_digit_number = input("Enter a two-digit number: ")

if len(two_digit_number) == 2 and two_digit_number.isdigit():
    sum_digit = int(two_digit_number[0]) + int(two_digit_number[1])
    print(f"Sum of digits in {two_digit_number} is {sum_digit}")
else:
    print("Enter a valid digit number")


# another method

# first_digit = int(two_digit_number[0])
# second_digit = int(two_digit_number[1])

# print(first_digit + second_digit)
