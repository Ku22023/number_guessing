pin = 5825
pin_attempts = 3
menu = False
user_return = 0
user_balance = 0

def check_balance():
    return user_balance

def withdraw():
    print("---WITHDRAW---")
    user_input = float(input("Enter how much you would like to "\
        "withdraw: "))
    if user_input > user_balance:
        return False

def deposit():
    pass

def transaction_history():
    pass

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
        menu = False
        user_balance = check_balance()
        print(f"\nCurrent Balance: ${user_balance}")
        while user_input != -1:
            user_input = int(input("Type -1 to return: "))
            if user_input == -1:
                menu = True
    elif user_input == 2:
        menu = False
        withdraw()
    elif user_input == 3:
        deposit()
    elif user_input == 4:
        transaction_history()
    elif user_input == 5:
        menu = False
        print("Goodbye!")
    else:
        print(f"\nError: {user_input} is not a valid option!\n")
