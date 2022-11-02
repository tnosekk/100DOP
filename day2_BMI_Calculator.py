# BMI Calculator

print("Welcome to the BMI calculator")

height = input("What is your height (in m):\n")
weight = input("What is your weight (in KG)\n")
sqr_height = pow(float(height), 2)

# BMI = weight/weight*weight

bmi = float(weight)/sqr_height

print(str(bmi) + "\n")
