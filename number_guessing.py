import random

def welcome():
    """
    This function starts the user and generates a random number
    """
    print("\n----- Number Guessing Game ------\n")
    user_name = str(input("- What is your name: \n"))
    print(f"Welcome {user_name}!\nIn this game, you have three tries to\
        guess a number 1-5.\nIf you get it wrong, the number changes\n\
        You need to guess five numbers correctly to win!")
    number = random.randrange(1,5)
    thegame(wins, guesses,number)

def thegame(wins, guesses, number):
    """
    The main code, checks if the number is right or wrong
    """
    game = True
    print(number)
    while game == True:
        if guesses >= 1:            
            user_guess = int(input(f"\n\n\nWins: {wins}\nGuess a \
                number between 1 and 5!\nYou have {guesses} guesse(s)\
                 left!\n"))
            try:
                user_guess + 1
            except ValueError:
                print("An error occured.")
                thegame(wins,guesses,number)
            if user_guess == number:
                print(f"Congratulations! You got it!")
                if wins != 4:
                    wins += 1
                    number = random.randrange(1,5)
                    thegame(wins,guesses,number)
                else:
                    print("You have beaten the game! Congrats!!")
                    game = False
                    user_guess = str(input("Type anything to play \
                        again. Type exit to exit!"))
                    if user_guess != "exit":
                        welcome()
                    else:
                        exit()
            else:
                guesses -= 1
                print(f"Wrong Number Please try again!")
                thegame(wins, guesses, number)

        else:
            print("Round lost! New number generated!")
            guesses = 3
            game = False
            random.randrange (1,5)
            thegame(wins,guesses,number)

wins = 0
guesses = 3
welcome()