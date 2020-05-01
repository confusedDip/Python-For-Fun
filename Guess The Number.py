import numpy as np

print('Welcome to "GUESS THE NUMBER"')
print("You have 10 chances to guess")
print("After each guess you will be told if the actual number is lesser or greater than your guess")
print("Let's start")
random_number = np.random.randint(0, 1000)
game_finish = False
game_win = False
game_over = True
round = 0
while not game_finish:
    round += 1
    print("Round ", round)
    guess = int(input("Guess The Number: "))
    if random_number > guess:
        print("The number is greater than your guess")
    elif random_number < guess:
        print("The number is lesser than you guess")
    else:
        game_win = True
        game_over = False
        game_finish = True
    if round == 10 and not game_win:
        game_finish = True
        game_over = True

if game_win:
    print("Hurrah! You have guessed it correct!")
elif game_over:
    print("Sorry! You could not guess it!")
