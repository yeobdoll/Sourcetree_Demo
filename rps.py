from random import randint

play = ["Rock", "Paper", "Scissors"]

computer = play[randint(0, 2)]
print('Computer: {}'.format(computer))

player = input("Rock, Paper, Scissors? ")
print('Player: {}'.format(player))

if player == computer:
    print("Tie!")
elif player == "Rock":
    if computer == "Scissors":
        print("You win!")
    else:
        print("You lose!")