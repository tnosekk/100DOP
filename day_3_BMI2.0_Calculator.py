height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = weight/(height ** 2)
bmi_round = round(bmi)

if bmi <= 18.5:
    print(f"Your BMI is {bmi_round}, you are underweight.")
elif 25 >= bmi > 18.5:
    print(f"Your BMI is {bmi_round}, you have a normal weight.")
elif 30 >= bmi > 25:
    print(f"Your BMI is {bmi_round}, you are slightly overweight.")
elif 30 >= bmi > 30:
    print(f"Your BMI is {bmi_round}, you are obese.")
else:
    print(f"Your BMI is {bmi_round}, you are clinicaly obese.")
