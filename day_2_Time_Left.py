age = input("What is your current age? ")

time_in_years = 90 - int(age)
time_in_days = int(time_in_years*365)
time_in_weeks = int(time_in_years*52)
time_in_months = int(time_in_years*12)

print(f"You have {time_in_days} days, {time_in_weeks} weeks, and {time_in_months} months left.")

