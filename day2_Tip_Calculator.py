print("Welcome to the tip calculator!")

bill = input("What was the total bill? $")
tip = input("How much tip would you like to give? 10, 12, or 15? ")
people = input("How meny people to split the bill? ")

bill_per_person = round(float(bill)/int(people), 3)
tip_per_person = round((float(bill)*int(tip))/100/int(people),2)
total_per_person = round(float(bill_per_person)+float(tip_per_person),2)

message = f"Each person should pay: ${total_per_person}"
print(message)