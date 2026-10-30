import random
item_list = ["Rock", "Paper", "Scissor"]
user = input("Enter your choice -> Rock, Paper, Scissor : ")
comp = random.choice(item_list)

print("Your choice : ", user, "\nComputer choice : ", comp)

if user == comp:
    print("Match Tie")

elif user == "Rock":
    if comp == "Paper":
        print("Paper wins.. u lost")
    else:
        print("Rock wins.. u won")

elif user == "Paper":
    if comp == "Rock":
        print("Paper wins.. u won")
    else:
        print("Scissor wins.. u lost")

elif user == "Scissor":
    if comp == "Paper":
        print("Scissor wins.. u won")
    else:
        print("Rock wins.. u lost")