print("Welcome to my computer quiz!")
# Asking to Play
playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()
else:
    print("Okay, Let's Play! \n")

# score
score = 0

# Question 1
user_input = input("What does RAM stand for? \n")
answer = user_input.lower()
if answer != "random access memory":
    print("Incorrect! \n")
else:
    print("Correct \n")
    score += 1

# Question 2
user_input = input("What does PSU stand for? \n")
answer = user_input.lower()
if answer != "power supply":
    print("Incorrect! \n")
else:
    print("Correct \n")
    score += 1

# Question 3
user_input = input("What does CPU stand for? \n")
answer = user_input.lower()
if answer != "central processing unit":
    print("Incorrect! \n")
else:
    print("Correct \n")
    score += 1

print(f"Your score is {score}")
print("Your percentage is " + str((score / 4) * 100))