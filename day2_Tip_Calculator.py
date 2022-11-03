print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How meny people to split the bill? "))

bill_per_person = round(bill / people, 3)
tip_per_person = round((bill * tip)/100/people, 2)
total_per_person = round(bill_per_person + tip_per_person, 2)
total_per_person = "{:.2f}".format(total_per_person)


message = f"Each person should pay: ${total_per_person}"
print(message)
