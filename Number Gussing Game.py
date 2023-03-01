import random

# Top Range Selection
# The if-else statement is there to make sure that the input is a valid number
top_of_range = input("What should be the top range? ")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number that is greater than 0")
        quit()
else:
    print("Please type a valid number next time")
    quit()

# Random number selection
random_number = random.randint(0, top_of_range)
guesses = 0

# User Guessing
while True:
    guesses += 1
    # The if-else statement is there to make sure that the input is a valid number
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)

        if user_guess <= 0:
            print("Please type a number that is greater than 0")
            quit()
    else:
        print("Please type a valid number next time")
        quit()

    # Verifying the number
    if user_guess == random_number:
        print("It Correct!")
        break
    else:
        if user_guess > random_number:
            print("You are above the given number")
        else:
            print("You are below the number")

print(f"The correct number was {random_number}")
print(f"You got it in {guesses} tries")
