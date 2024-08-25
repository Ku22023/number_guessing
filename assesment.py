pin = 5825
pin_attempts = 3
menu = False
user_balance = 0
transactions = [] #Transaction list to show when the user requests \
#it.
prevent_none = True

def check_balance():
    """
    Checks the amount of money in the user_balance variable, to show
    the user how much the variable is.
    """
    print("\n---BALANCE---")
    return user_balance

def withdraw(user_balance):
    """
    Checks the amount of money in user_variable, and if there is enough,
    it removes money from the user_balance variable and updates to for 
    a "withdrawal".
    """
    print("---WITHDRAW---")
    try: #Ensures the user enters in a number
        user_input = float(input("Enter how much you would like to "\
            "withdraw: $")) #A float because it can handle decimals
        if user_input < 0: #Prevents the user from trying to \
            #withdraw less than $0.
            print("\nError: You cannot withdraw less then $0!")
        else:
            if user_balance == 0:
                print("Error: You do not have enough to withdraw!")
                user_balance = 0 #prevents user_balance from being \
                #'None'
                return user_balance  
            elif user_input > user_balance: #Prevents the user from \
                #withdrawing more than they have in their balance.
                print("Error: You do not have enough to withdraw!")
                return user_balance
            else:
                user_balance -= user_input
                print(f"Withdrew ${user_input} from your account!\n"
                f"Current Balance: {user_balance}")
                transactions.append(f"Withdrew ${user_input}") #Adds \
                #transaction to the list to show later, for the log.
                return user_balance
    except ValueError: #Prevents the user from entering anything but a \
        #number.
        print("\nError: Please enter a number!")

def deposit(user_balance):
    """
    Adds the user_input amount into the balance variable, then returns
    it to update the main user_balance variable, so that the money is
    added onto the main amount.
    """
    print("---DEPOSIT---")
    try: #Prevents the user from entering a letter.
        user_input = float(input("Enter how much you would like to "\
            "deposit: $"))
        if user_input < 0: #Prevents the user from entering \
            #negative money.
            print("\nError: You cannot deposit less than $0!")
        else:
            user_balance += user_input
            print(f"Deposited ${user_input} into your account!\n"
            f"Current Balance: {user_balance}")
            transactions.append(f"Deposited ${user_input}") #Adds the \
            #transaction to the transaction list, to show later.
            return user_balance
    except ValueError: #Runs the code again to stop it erroring out, if\
        #the user enters a letter.
        print("\nError: Please enter a number!")

def transaction_history():
    """
    Prints a list to show everything in it. The list contains sentences
    like: "Deposited {user_input}!". The i loop just shows this list
    in a clean way.
    """
    print("---TRANSACTION HISTORY---")
    for i in transactions: #The for loop is to show each transaction \
        #on its own line, instead of in the list variable
        print(i)
    print("---END OF LIST---")

def back(menu):
    """
    This function runs after every other function, to make the user
    confirm to go back to the main menu. I made this because it makes
    the output look cleaner, and give the user time to proccess the
    information before going back to the main menu
    """
    user_input = 0
    while user_input != -1:
        try: #Prevents the user from entering a number.
            user_input = int(input("Type -1 to return: "))
            if user_input == -1: #Makes sure the number is -1 to \
                #return
                menu = True
                return menu
        except ValueError: #Asks the user again, if the user doesn't \
            #enter -1 or if the user enters a letter.
            print("Error: Please type -1!")



print("Card Inserted!")
while pin_attempts > 0: #Asks the pin until they have no more tries.
    try: #Prevents the user from entering in letters.
        user_input = int(input("Please enter your pin: "))
        if user_input == pin: #Checks if the PIN is correct.
            menu = True
            print("Access Granted!")
            print("\nWelcome {user!} to the ATM!") #To make it look \
            #nice.
            pin_attempts = 0 #Stops the ATM from asking for the PIN \
            #again
        else:
            print(f"Error: Incorrect PIN. You have {pin_attempts - 1}" \
                " attempt(s) remaining.") #If the user gets it wrong,
            #it asks again until they have no more tries left.
            pin_attempts -= 1
    except: #Prevents the user from typing in a letter.
            print("Error: You must enter a number!")

while menu == True: #To always open the menu if no code is running.
    try: #Prevents the user from typing in a letter.
        user_input = int(input("\nChoose your option:\n-1. Check " \
        "Balance \n-2. Withdraw \n-3. Deposit \n-4. Transaction" \
        " History \n-5. Exit\n"))
        if user_input == 1:
            user_balance = check_balance()
            print(f"Current Balance: ${user_balance}")
        elif user_input == 2:
            user_balance = withdraw(user_balance)
        elif user_input == 3:
            user_balance = deposit(user_balance)
        elif user_input == 4:
            transaction_history()
        elif user_input == 5:
            menu = False
            print("Goodbye!")
            exit()
        else: #Runs the code again if the number is not a valid option
            print(f"\nError: {user_input} is not a valid option!\n")
        try: #Without this, if the user_balance is 0, it would be set \
        #to 'None', which breaks the code.
            user_balance + 1
        except:
            user_balance = 0 #Sets user_balance to '0', instead of 'None'
        menu = False #Make the menu close after input
        menu = back(menu)
    except ValueError: #Prevents the user from entering a letter
        print("Error: You must enter a number!")