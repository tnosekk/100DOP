import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
symbol = [rock, paper, scissors]

player_choice = int(input("What do you chose? 0 for Rock, 1 for Paper, 2 for Scissors\n"))
computer_choice = random.randint(0, 2)

if player_choice >= 3:
    print("You choose a wrong number, try again.")
else:
    print(symbol[player_choice])
    print(f"Computer choose:\n{symbol[computer_choice]}")

##############player choose rock###############
if player_choice == 0 and computer_choice == 2:
    print("You win!")
elif player_choice == 0 and computer_choice == 1:
    print("You loose!")
elif player_choice == 0 and computer_choice == 0:
    print("You draw!")
##############player choose paper###############
elif player_choice == 1 and computer_choice == 0:
    print("You win")
elif player_choice == 1 and computer_choice == 2:
    print("You loose!")
elif player_choice == 1 and computer_choice == 1:
    print("You draw!")
#############player choose scissors#############
elif player_choice == 2 and computer_choice == 1:
    print("You win")
elif player_choice == 2 and computer_choice == 0:
    print("You loose")
elif player_choice == 2 and computer_choice == 2:
    print("You draw!")



