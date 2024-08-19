grocery_list = []

def add_item():
    user_input = str(input("What would you like to add? "))
    grocery_list.append(user_input)
    print(grocery_list)
    print(f"{user_input} has been added to your cart!")

def remove_item():
    pass

def view_list():
    pass

def check_list():
    pass

print("Welome to the grocery store!")
menu = True
while menu == True:
    user_input = int(input("What would you like to do?\n-1. Add item"
            "\n-2. Remove item\n-3. View grocery list\n-4. Check if"
            " item is on list\n-5. Quit\n"
            ))
    if user_input == 1:
        add_item()
    elif user_input == 2:
        remove_item()
    elif user_input == 3:
        view_list()
    elif user_input == 4:
        check_list()
    elif user_input == 5:
        print("Goodbye!")
        menu = False
    else:
        print(f"\nError: '{user_input}' is not a valid option!")