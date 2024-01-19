current_age = input("Enter your current age: ")
total_age = 90
remaining_age = 90 - int(current_age)
days = 365*remaining_age
weeks = 52*remaining_age
months = 12*remaining_age

print(f"You have {days} days, {weeks} weeks, and {months} months  left")
