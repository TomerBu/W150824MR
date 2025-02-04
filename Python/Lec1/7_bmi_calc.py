weight = int(input("Enter your weight in kg: "))
height = int(input("Enter your height in cm: ")) / 100

bmi = weight / height ** 2

if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal weight")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")


if bmi < 18.5:
    print("Underweight")
elif 18.5 <= bmi < 25:
    print("Normal weight")
elif bmi >= 25 and bmi < 30:
    print("Overweight")
else:
    print("Obese")
