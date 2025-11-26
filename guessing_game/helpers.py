import sys

# helper functions
def quitGame():
    game_end = input("Are you ready to quit?: ")
    if game_end == "Yes" or game_end == "yes" or game_end == "y":
        sys.exit()
    elif game_end == "No" or game_end == "no" or game_end == "n":
        print("Ok!")
    else:
        print("That's not a real answer!")
