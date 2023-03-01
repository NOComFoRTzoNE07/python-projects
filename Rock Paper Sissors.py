import random

user_wins = 0
computer_wins = 0
options = ["rock", "paper", "scissors"]

while True:
    # Checking whether the user has given the correct response
    user_response = input("Type rock / paper / scissors or Q to quit: \n").lower()
    if user_response == "q":
        break

    if user_response not in options:
        continue

    # Starting to play the game
    random_number = random.randint(0, 2)
    computer_pick = options[random_number]
    print(f"The computer picked {computer_pick}")

    if user_response == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1

    elif user_response == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1

    elif user_response == "scissors" and computer_pick == "paper":
        print("You won! \n")
        user_wins += 1

    else:
        print("You lost! \n")
        computer_wins += 1

print(f"You won {user_wins} times")
print(f"The computer won {computer_wins} times")
print("Thank you for playing!")
