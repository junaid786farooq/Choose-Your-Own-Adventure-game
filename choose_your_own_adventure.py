# Code for adventure game for user.

name = input("What is your name:\n").capitalize()

print(f"Welcome {name} to this adventure.")

answer = input(f"{name} You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go?\n").lower()

if answer == "left":
    answer = input(f"{name} You come to a river, you can walk around it or swim accross? Type walk to walk around and swim to swim accross:\n").lower()

    if answer == "swim":
        print(f"{name} You swam acrross and were eaten by an alligator. You lose!")
    elif answer == "walk":
        print(f"{name} You walked for many miles, ran out of water and you lost the game!")
    else:
        print("Not a valid option. You lose!")

elif answer == "right":
    answer = input(f"{name} You come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)?\n").lower()

    if answer == "back":
        print(f"{name} You go back and lose!")
    elif answer == "cross":
        answer = input(f"{name} You cross the bridge and meet a stranger. Do you talk to them (yes/no)?\n").lower()
        if answer == "yes":
            print(f"{name} You talk to the stanger and they give you gold. You WIN!")
        elif answer == "no":
            print(f"{name} You ignore the stranger and they are offended and you lose.")
        else:
            print(f"{name} Not a valid option. You lose!")
    else:
        print(f"{name} Not a valid option. You lose!")
    

else:
    print(f"{name}Not a valid option. You lose!")

print("Thank you for trying", name)