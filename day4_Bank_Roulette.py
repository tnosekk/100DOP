import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ") #tworzenie listy z podnaych elementów

num_of_names = len(names) - 1
random_number = random.randint(0, num_of_names)
chosen = names[random_number]

print(f"{chosen} is going to buy the meal today!")


# inaczej można też użyć komendy random.choice(names) :))))