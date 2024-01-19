hieght = input("Enter your hieght in meter: ")
wieght = input("Enter your wieght in kg: ")

hieght = float(hieght)
wieght = int(wieght)


age = round(wieght/hieght**2)

print(f"Your age is {age}")
