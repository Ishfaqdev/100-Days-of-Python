print("Welcome to the Tip Calculator.")

total_bill = int(input("What was the total bill? $"))

tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))

total_tip = (tip / 100) * total_bill

total_tip = total_tip + total_bill

total_people = int(input("How many people to split the bill?  "))

each_person_pay = round(total_tip / total_people, 2)

print(f"Each person should pay : ${each_person_pay}")
