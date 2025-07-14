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

images_list = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
print(images_list[user_choice])

computer_choice = random.randint(0,2)
print(f"Computer chose:")
print(images_list[computer_choice])

if user_choice == 0 and computer_choice == 2:
    print("Rock crushes scissors! You win!")
elif user_choice == 2 and computer_choice == 1:
    print("Scissors cuts paper! You win")
elif user_choice == 1 and computer_choice == 0:
    print("Paper covers rock! You win!")
elif user_choice == computer_choice:
    print("Try again, it's a draw ")
else:
    print("You lose!")