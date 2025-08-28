Correct = "burnbot"

password = input("Enter the password: ")
if password == Correct:
    print("Access granted")
else:
    print("Access denied")
    exit()

print("Welcome to burnbot")

name = input("What is your name?")
print(f"Hello, {name}")

answer = input("Are you ready?(yes/no)").lower().strip()
if answer == "yes":
    print("Continue and answer these questions below.")
elif answer == "no":
    print("Commitment issues I see.")
    exit()
else:
    print("Answer denied")
    exit()

Age = input("How old are you?")
Color = input("What is your favorite color?")
Food = input("What is your favorite food?")
Hobby = input("What do you do for fun?")
Game = input("What is your favorite game?")
Show = input("What's your favorite show?")

print("Thinking of response...")
import random

choices = ["Couldn't think of anything, you're pretty cool.", 
f"You're {Age} still {Hobby}, get a life and take a shower. And not to mention you watch {Show}, what a terrible choice, you must be lonely.", 
f"No way your favorite color is {Color}, it's like you're still a child. You're {Age} and play {Game} grow up, and {Food} is disgusting."]
selected = random.choice(choices)
print(selected)

answer = input("Would you like to rate this game?").lower().strip()
if answer == "yes":
    print("Thank you:")
elif answer == "no":
    print("Someone got their feelings hurt didn't they")
    exit()
else:
    print("Answer denied")
    exit()

rate = int(input("What do you rate this experince 1-10"))
if 1 <= rate <= 6:
    print("We don't really care about your rating anyway.")
elif 7<= rate <= 10:
    print("We're glad you enjoyed burnbot.")
else:
    print(f"we said 1-10 not {rate}")