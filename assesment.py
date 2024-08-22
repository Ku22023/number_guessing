pin = 5825
pin_attempts = 3
menu = False
user_return = 0
user_balance = 0
transactions = []

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
    try: #Without this, if the user_balance is 0, it would be set to \
        #'None', which breaks the code
        user_balance + 1
    except:
        user_balance = 0
    print("---WITHDRAW---")
    user_input = float(input("Enter how much you would like to "\
        "withdraw: "))
    if user_input > user_balance:
        print("not enough money D:")
    else:
        user_balance -= user_input
        print(f"Withdrawn ${user_input} from your account!\n"
        f"Current Balance: {user_balance}")
        transactions.append(f"Withdrew ${user_input}")
        return user_balance

def deposit(user_balance):
    """
    Adds the user_input amount into the balance variable, then returns
    it to update the main user_balance variable, so that the money is
    added onto the main amount.
    """
    print("---DEPOSIT---")
    user_input = float(input("Enter how much you would like to "\
        "deposit: "))
    user_balance += user_input
    print(f"Deposited ${user_input} into your account!\n"
    f"Current Balance: {user_balance}")
    transactions.append(f"Deposited ${user_input}")
    return user_balance

def transaction_history():
    """
    Prints a list to show everything in it. The list contains sentences
    like: "Deposited {user_input}!". The i loop just shows this list
    in a clean way.
    """
    print("---TRANSACTION HISTORY---")
    for i in transactions:
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
        user_input = int(input("Type -1 to return: "))
        if user_input == -1:
            menu = True
            return menu

print("Card Inserted!")
while pin_attempts > 0:
    user_input = int(input("Please enter your pin: "))
    if user_input == pin:
        menu = True
        print("Access Granted!")
        print("\nWelcome {user!} to the ATM!")
        pin_attempts = 0
    else:
        print(f"Error: Incorrect PIN. You have {pin_attempts - 1}" \
            " attempt(s) remaining.")
        pin_attempts -= 1

while menu == True:
    user_input = int(input("\nChoose your option:\n-1. Check Balance"
    "\n-2. Withdraw \n-3. Deposit \n-4. Transaction History \n-5. Exit"
    "\n"))
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
        print("Goodbye!")
        exit()
    else:
        print(f"\nError: {user_input} is not a valid option!\n")
    menu = False
    menu = back(menu)