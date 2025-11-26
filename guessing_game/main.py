# imports
import random
import helpers

# rng
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num = random.choice(num_list)

# game proper
answer = input("Are you ready to play the number guessing game?: ")
if answer == "Yes" or answer == "yes" or answer == "y":
    while True:
        guess = int(input("Pick a number from 1 through 10: "))
        if guess == num:
            print(f"The number was {num} so you won. Good job!")
            helpers.quitGame()
        else:
            print(f"The number was {num} so you lost. Better luck next time.")
            helpers.quitGame()
elif answer == "No" or answer == "no" or answer == "n":
    print("Ok, see you next time!")
else:
    print("Please give proper input on the next execution of this program!")
