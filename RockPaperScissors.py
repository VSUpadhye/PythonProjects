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

game_images = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors:\n"))
if user_choice >= 0 and user_choice <= 2:
    print(game_images[user_choice])
comp_choice = random.randint(0, 2)
print(f"Computer chose: {game_images[comp_choice]}")

if user_choice >= 3 or user_choice < 0:
    print("You typed invalid number. You lose!")
elif user_choice == 0 and comp_choice == 2:
    print("You win!")
elif comp_choice == 0 and user_choice == 0:
    print("You lose!")
elif user_choice > comp_choice:
    print("You win!")
elif comp_choice > user_choice:
    print("You lose!")
elif user_choice == comp_choice:
    print("It's a draw!")