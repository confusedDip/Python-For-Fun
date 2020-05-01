import numpy as np


def intro():
    print("Welcome to our very favorite game STONE PAPER and SCISSOR")
    print("Rules are pretty simple")
    print("Stone breaks Scissor")
    print("Scissor cuts Paper")
    print("Paper covers stone")
    print("You will play against customised opponent")
    print("The one to score 5 first wins")
    print("Shall we begin?")

    print("Enter your name: ")
    player_name = input("> ")
    print("Enter your opponent's name:")
    computer_name = input("> ")
    return player_name, computer_name


game = ["stone", "paper", "scissor"]
player, computer = intro()
player_score = 0
computer_score = 0
rounds = 0
while computer_score < 5 and player_score < 5:
    rounds += 1
    print("Round ", rounds)
    print("Stone, Paper or Scissors?")
    player_choice = input("> ").lower()
    computer_choice = game[np.random.randint(0, 2)]
    if player_choice == "stone" and computer_choice == "paper":
        computer_score += 1
        print("Paper of ", computer, " covers the stone of ", player)
    elif player_choice == "stone" and computer_choice == "scissor":
        player_score += 1
        print("Stone of ", player, " breaks the scissor of ", computer)
    elif player_choice == "paper" and computer_choice == "stone":
        player_score += 1
        print("Paper of ", player, " covers the stone of ", computer)
    elif player_choice == "scissor" and computer_choice == "stone":
        computer_score += 1
        print("Stone of ", computer, " breaks the scissor of ", player)
    elif player_choice == "scissor" and computer_choice == "paper":
        player_score += 1
        print("Scissor of ", player, " cuts the paper of ", computer)
    elif player_choice == "paper" and computer_choice == "scissor":
        computer_score += 1
        print("Scissor of ", computer, " cuts the paper of ", player)
    else:
        print("Draw!")
    print("After round ", rounds)
    print(player, ": ", player_score, " ", computer, ": ", computer_score)
    print("\n")

if player_score == 5:
    print(player, " Wins!")
else:
    print(computer, " Wins!")
