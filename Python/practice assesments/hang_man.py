import random
word_list = ["jacky", "mo", "omar", "davidson", "brimely","tsai", "boba", "ryan", "roid", "kim"]

def ran_word():
    letters = []
#chooses random word
    random_num = random.randint(0, len(word_list) - 1) #gets a random number from the list to grab a random item
    hangman_word = word_list[random_num] #grabs random word
    #breaks the word up into individual letters
    return hangman_word
    for i in letters: #redundant, delete later
        print(i)
    return letters #bring letters back to functions

def game(word):
    lives = 6
    letters = list(word)
    used_name = []
    guess = []
    guessed_stuff = []
    for i in letters:
        guess.append(" _ ")
    print(guess)
    print(letters) #shows the list of letters for the hangman
    active = True
    while active == True:
        user_input = str(input("Type in a or word: "))
        if user_input in set(used_name):
            print ("you already guessed that")
        else:
            used_name.append(user_input)
            if len(user_input) == 1:
                guessed_stuff.append(user_input)
                print("letters n stuff: ",guessed_stuff)
                if user_input in set(letters): #checks if letter is right
                    print("correct!!")
                    space = (letters.index(user_input))
                    guess[space] = user_input
                    print(guess)
                else:
                    print("wrong!!!")

word = ran_word()
game(word)

# |_______
# |      |
#        o 
#       /|\
#       / \
# |____________
#
#
#
