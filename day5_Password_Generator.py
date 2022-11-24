import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
           'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
           'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = []
let_len = len(letters) - 1
for i in range(0, nr_letters):
    random_letter = letters[random.randint(0,let_len)]
    password.append(random_letter)  

symb_len = len(symbols) - 1
for i in range(0, nr_symbols):
    random_symb = symbols[random.randint(0,symb_len)]
    password.append(random_symb)
    
num_len = len(numbers) - 1
for i in range(0, nr_numbers):
    random_num = numbers[random.randint(0,num_len)]
    password.append(random_num)

random.shuffle(password)

print("Your password is:")
print(*password, sep='')

