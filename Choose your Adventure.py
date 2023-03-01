name = input("What is your name: \n")
print(f"Welcome {name} to this adventure!")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. "
               "Which way do you want to go? \n").lower()

# Left side Quests
if answer == "left":
    left_quest = input("You come to the river, you can walk around it or swim across? "
                       "Type walk to walk around and swim to swim across. \n").lower()

    if left_quest == "swim":
        print("You swim across and get eaten by a crocodile")
    elif left_quest == "walk":
        print("You walked for many miles, ran out of water and lost the game!")
    else:
        print("Not a valid answer. You lose!")

# Right side quests
elif answer == "right":
    right_quest = input("Do you want to cross it or head back? Cross/Back \n").lower()

    if right_quest == "cross":
        # Right side inside Quest
        right_inside_quest = input("You cross the bridge and met a stranger. Do you want to talk to them? "
                                   "Yes / No \n").lower()

        if right_inside_quest == "yes":
            print("You win because you got the treasure!")
        elif right_inside_quest == "no":
            print("You lose because that stranger had the treasure!")
        else:
            print("Not a valid answer. You lose!")

    elif right_quest == "back":
        print("You got back and lost")
    else:
        print("Not a valid answer. You lose!")

else:
    print("Not a valid answer. You lose!")






