import random

def welcome():
    print("\n----- Number Guessing Game ------\n")
    user_name = str(input("- What is your name: \n"))
    print(f"Welcome {user_name}!\nIn this game, you have three tries to guess a number 1-5.\nIf you get it wrong, the number changes\nYou need to guess five numbers correctly to win!")
    thegame(rounds, wins)
def thegame(rounds, wins):
    game = True
    guesses = 3
    tries = 1
    while game == True:
        if guesses >= 1:
            user_guess = int(input(f"\n\nRound {rounds}\nWins: {wins}\nGuess a number between 1 and 5!\nYou have {guesses} guesse(s) left!\n")) 
            number = 1 
            number = random.randrange(1,5)
            if user_guess == number:
                print(f"Congratulations! You got it in {tries} tries!")
                game = False
                if wins != 4:
                    wins += 1
                    thegame(rounds, wins)
                else:
                    print("You have beaten the game! Congrats!!")
            else:
                tries += 1
                guesses -= 1
                print(f"Wrong Number Please try again!")
                thegame(rounds, wins)
            rounds += 1
        else:
            print("Game over! Please try again!!")
            game = False

rounds = 1
wins = 0
welcome()