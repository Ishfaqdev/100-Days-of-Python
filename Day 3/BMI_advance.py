hieght = float(input("Enter your hieght in m: "))
wieght = float(input("Enter your wieght in kg: "))

bmi = round(wieght/(hieght**2))

"""
Underweight: BMI less than 18.5
Normal weight: BMI between 18.5 and 25
Overweight: BMI between 25 and 30
Obese: BMI of between 30 35
Clinically: BMI 35 or greater

"""
if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight")
elif bmi < 25:
    print(f"Your BMI is {bmi}, your weight is normal")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are abese")
else:
    print(f"Your BMI is {bmi}, you are clinically abese")
