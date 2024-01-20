print("Welcome to the rollercoaster!")

hieght = int(input("What is your hieght in cm? "))

if hieght >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age "))
    if age < 12:
        print("Please pay $5")
    elif age <= 18:
        print("Please pay $7")
    else:
        print("Please pay $12")
else:
    print("Sorry! You have to grow taller before you can ride")
