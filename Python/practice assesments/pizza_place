
order = []

def backor():
    x = int(input("\nEnter -1 to go back: "))
    if x == -1:
        orders()
    else:
        backor()

def backst():
    x = int(input("\nEnter -1 to go back: "))
    if x == -1:
        start()
    else:
        backst

def menu():
    #You should display a menu here! Make it look pretty!
    print("----------- MENU -----------\n")
    print("[ #1. Mo's Special --- $16.30 ]\n - Random toppings; You get a surprise!\n")
    print("[ #2. Peperroni --- $12.50 ]\n - Classic Peperroni Pizza\n")
    print("[ #3. Cheese --- $9.99 ]\n - Classic Pizza with no toppings\n")
    print("[ #4. Skibidi Slicers --- $19.99 ]\n - a Pizza with all the toppings!\n")
    print("[ #5. Meat Lovers --- $14.99 ]\n - Lots of meaty mo's\n")
    print("[ #6. Vegetarian --- $12.99 ]\n - Vegetarian Option")
    backst()

def vieworder():
    k = 0
    l = 0
    print("\n--- Your current order contains: ---\n")
    for i in order:
        k += 1
        if i == 1:
            j = "Mo's Special - $16.30"
            l += 16.30
        if i == 2:
            j = "Peperroni Pizza - $12.50"
            l += 12.50
        if i == 3:
            j = "Cheese Pizza - $9.99"
            l += 9.99
        if i == 4:
            j = "Skibidi Slicers - $19.99"
            l += 19.99
        if i == 5:
            j = "Meat Lovers - $14.99"
            l += 14.99
        if i == 6:
            j = "Vegetarian - $12.99"
            l += 12.99
        print(f"{k}. {j}")
    print(f"\nThe total cost of your items is ${l}\n")
    
    	
def orders():
    user_exit_a = False
    while user_exit_a != True:
        print("\n----- Choose order Option: -----\n- 1. View order \n- 2. Add item(s) \n- 3. Remove item(s)\n- 4. Back to Main Menu")
        y = int(input("Select an option: "))
        if y == 1:
            vieworder()
            backor()
        if y == 2:
            x = 1
            print("\n")
            while x != -1:
                if x != -1:
                    if x >= 1 and x <= 6:
                        x = int(input("Enter which Pizzas you would like to order. Type -1 to finish: "))
                        order.append(x)
                    else:
                        print("Error: Invalid Item. Please enter a number 1-6")
                        order.pop()
                        orders()
            order.pop()
            print()
            print(f"\n --- Order Complete! --- \n")
            orders()
        if y == 3:
            x = 0
            while x != -1:
                item = "error"
                x = int(input("\nEnter the place of the item you want to remove, from the order list. Type -1 when you are finished: "))
                print(x)
                if x != -1:
                    x -= 1
                    print(f"Removed item number {x} from the list.)")
                    order.pop(x)
                elif x == -1:
                    orders()
        if y == 4:
            start()
        user_exit_a = True


def total():
    cost = 0
    k = 0
    #look through their order list and calculate the cost
    print("\n--- Your current order contains: ---\n")
    for i in order:
        k += 1
        if i == 1:
            j = "Mo's Special - $16.30"
            cost += 16.30
        elif i == 2:
            j = "Peperroni Pizza - $12.50"
            cost += 12.50
        elif i == 3:
            j = "Cheese Pizza - $9.99"
            cost += 9.99
        elif i == 4:
            j = "Skibidi Slicers - $19.99"
            cost += 19.99
        elif i == 5:
            j = "Meat Lovers - $14.99"
            cost += 14.99
        elif i == 6:
            j = "Vegetarian - $12.99"
            cost += 12.99
        print(f"{k}. {j}")
    print(f"\nThe total cost of your items is ${cost}\n")
    backst()

    
def start():
    user_exit = False
    while user_exit != True:
        print("\n--------Start-------\n- 1. Menu \n- 2. Order \n- 3. Calculate Total \n- 4. Exit\n--------------------")
        user_input = int(input("Choose what you want: \n"))
        if user_input == 1:
            menu()
        if user_input == 2:
            orders()
        if user_input == 3:
            total()
        if user_input == 4:
            print("\nThanks for stopping by!\n")
        user_exit = True


    #Your code can go here
    #You may want to add to this if statement 

print("Welcome to the Pizza Store")
print("Please pick what you would like to do!")
start()
