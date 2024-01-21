print("Welcome t Python Pizza Deliveries!")

size = input("What size of Pizza do you want to deliver? S, M, or L : ").upper()
add_pepperoni = input("Do you want to pepperoni? Y or N : ").upper()
extra_cheese = input("Do you want to extra cheese? Y or N : ").upper()

pizza_price = 0

if size == "S":
    pizza_price = 15
elif size == "M":
    pizza_price = 20
else:
    pizza_price = 25

if add_pepperoni == "Y":
    if size == "S":
        pizza_price += 2
    else:
        pizza_price += 3

if extra_cheese == "Y":
    pizza_price += 1

print(f"Your final bill is ${pizza_price}")
