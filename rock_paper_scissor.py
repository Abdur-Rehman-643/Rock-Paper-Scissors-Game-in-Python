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
game_combinations = ['rock','paper','scissors']
game_combinations_images = [rock,paper,scissors]
user_input = -1
while (user_input < 0) or (user_input > 2):
    try:
        user_input = int(input("Please enter a number between 0 and "
                               "2 (0 for rock 1 for paper 2 for scissors) : "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")

print(f"You choose {game_combinations[user_input]} \n")
print(game_combinations_images[user_input])

computer_input = random.randint(0,2)

print(f"Computer choose {game_combinations[computer_input]} \n")
print(game_combinations_images[computer_input])

if user_input == computer_input:
    print("Tie (no winner)")
elif user_input == 0 and computer_input == 1:
    print("Computer win")
elif user_input == 0 and computer_input == 2:
    print("You win")
elif user_input == 1 and computer_input == 0:
    print("You win")
elif user_input == 1 and computer_input == 2:
    print("Computer Wins")
elif user_input == 2 and computer_input == 1:
    print("You win")
elif user_input == 2 and computer_input == 0:
    print("Computer Wins")