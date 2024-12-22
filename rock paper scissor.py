import random

options = ("rock","paper","scissors")

running = True
while running:
    player = None
    computer = random.choice(options)
    while player not in options:
        player = input("enter a choice(rock, paper, scissors) : ")

    print(f"player:{player}")
    print(f"computer:{computer}")
    if player == computer:
        print("its a tie")
    elif player == "rock" and computer == "scissors":
        print("You win")
    elif player =="paper" and computer == "rock":
        print("you win")
    elif player =="scissor" and computer == "paper":
        print("you win")
    else:
        print("you lose")
    if not input("play again? (y/n) : ").lower() == "y":
        break
print("thank you")
