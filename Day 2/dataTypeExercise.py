two_digit_number = input("Type a two digit number: ")
if len(two_digit_number) == 2 and two_digit_number.isdigit():
    digit_sum = int(two_digit_number[0]) + int(two_digit_number[1])
    print(f"The sum of the digts in {two_digit_number} is {digit_sum}")
else:
    print("Please enter a valid 2-digit number")
