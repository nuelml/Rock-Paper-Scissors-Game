import random

rpc = ["""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""", """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""", """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""]


while True:
    
    choices = ["Rock", "Paper", "Scissors"]
    random_number = random.randint(0, len(rpc)-1)
    user_input = int(input("Choose you game! Enter 0 for Rock, 1 for Paper, and 2 for Scissors: "))
    
    if user_input not in [0, 1, 2]:
        print("Enter a valid number!")
        break

    elif user_input == random_number:
        print(f"Computer choose: {choices[random_number]}")
        print(rpc[random_number])
        print(f"You choose: {choices[user_input]}")
        print(rpc[user_input])
        print("Draw!")
        
    elif user_input == 0 and random_number == 2:
        print(f"Computer choose: {choices[random_number]}")
        print(rpc[random_number])
        print(f"You choose: {choices[user_input]}")
        print(rpc[user_input])
        print("You Won!")
        
    elif user_input == 2 and random_number == 1:
        print(f"Computer choose: {choices[random_number]}")
        print(rpc[random_number])
        print(f"You choose: {choices[user_input]}")
        print(rpc[user_input])
        print("You Won!")
        
    elif user_input == 1 and random_number == 0:
        print(f"Computer choose: {choices[random_number]}")
        print(rpc[random_number])
        print(f"You choose: {choices[user_input]}")
        print(rpc[user_input])
        print("You Won!")

    else:
        print(f"Computer choose: {choices[random_number]}")
        print(rpc[random_number])
        print(f"You choose: {choices[user_input]}")
        print(rpc[user_input])
        print("You lost!")