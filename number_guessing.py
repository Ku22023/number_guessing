import random

def welcome():
    print("\n----- Number Guessing Game ------\n")
    user_name = str(input("- What is your name: \n"))
    print(f"Welcome {user_name}!\nIn this game, you have three tries to guess a number 1-5.\nIf you get it wrong, the number changes\nYou need to guess five numbers correctly to win!")
    game()

def game():
    try:
        print(rounds)
    except NameError:
        rounds = 1
    game = True
    guesses = 3
    tries = 1
    while game == True:
        if guesses >= 1:
            user_guess = int(input(f"Round {round}\nGuess a number between 1 and 5!\nYou have {guesses} guesse(s) left!\n"))  
            number = random.randrange(1,5)
            print(number)
            if user_guess == number:
                print(f"Congratulations! You got it on the {tries} tries!")
                game = False
                rounds += 1
                game()
            else:
                tries += 1
                guesses -= 1
                print(f"WRONG!!!")


welcome()
