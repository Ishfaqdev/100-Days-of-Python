print("Welcome to the rollercoaster!")

hieght = int(input("What is your hieght in cm? : "))
bill = 0
if hieght >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? : "))
    if age < 12:
        bill = 5
        print("Childs tickets are $5")
    elif age < 18:
        bill = 7
        print("Youth tickets are $7")
    else:
        bill = 12
        print("Adults tickets are $12")
    wants_photo = input("Do you want taken a photo? Y or N : ")
    if wants_photo == "Y":
        bill += 3
        print(f"Your final bill is ${bill}.")
else:
    print("Sorry! You to grow taller befor you can ride")
