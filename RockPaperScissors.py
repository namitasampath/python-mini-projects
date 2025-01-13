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
game_img=[rock,paper,scissors]
user_input=int(input("What do you choose. Choose 0 for Rock, 1 for Paper, 2 for Scissors"))
if user_input >=0 and user_input<=2:
    print(game_img[user_input])
computer_choice=random.randint(0,2)
print(f"Computer choice is : {computer_choice}")
print(game_img[user_input])

if user_input == 0 and computer_choice == 2:
    print("You win")
elif user_input >= 3 or user_input < 0:
    print("Invalid number. You lose")
elif computer_choice== 0 and user_input==2:
    print("You lose")
elif user_input > computer_choice:
    print("You win")
elif computer_choice==user_input:
    print("Draw")

