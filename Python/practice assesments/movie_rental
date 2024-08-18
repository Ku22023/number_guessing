
rented_movies = ["deadpoolandwolverine","civilwar","skibiditoilet"] #what the user cannot currently rent because its taken out
movies = ["storyofjackymo","despicableme4","insideout2","aquietplace"] #the library of movies the user can currently rent
rental_keeper = {} #dictionary is created to track how many times a movie is taken out
for i in rented_movies:
    rental_keeper.update({i: 1}) #adding rented out once to every movie, because they are already rented out
for i in movies:
    rental_keeper.update({i: 2})
reportlist = []  

def start(): # start function menu so i can go back to it easily
    user_exit = False
    while user_exit != True:
        try:
            print("\n----- Movie Rentals -----\n")
            user_input = int(input("Choose your option: \n1 - Search for a Movie \n2 - Rent a Movie \n3 - Return a Movie \n4 - Admin Access\n5 - Exit\n\n"))
            if user_input == 1:
                search_movies()
            elif user_input == 2:
                rent_movies()
            elif user_input == 3:
                return_movies()
            elif user_input == 4:
                admin_menu()
            elif user_input ==  5:
                print("Thanks for stopping by!")
                exit()
            else:
                print(f"Error: {user_input} is not an option!") # stops the user from putting in a random number and breaking the system
                start()
            user_exit = True
        except ValueError:
            print(f"Error: that is not a vaild option!")
            start()
        except:
            print("An error occured")
            start()
                     
def search_movies():                     
    user_exit = False                     
    while user_exit != True:  
        try:                   
            user_input = str(input("Enter the title of the movie you would like to search up.\nType 'Finish' to return: "))                     
            title = user_input.lower()                     
            title = title.replace(" ", "") #makes it easier to search for, because everything is stored in lowercase with no spaces        
            if title != "finish":    
                if user_input in set(movies):   #sees if the movie is available in the library because its ez                   
                    print(f"\n{user_input} is currently available!\n")                     
                elif user_input in set(rented_movies):            #sees if movie is not in library but is being rented
                    print(f"\n{user_input} is currently being rented.\n")                     
                else:                    #if movie is not in library or is being rented
                    print(f"\nUnfortunately, we do not have {user_input} :(\n")                     
            else:                     
                user_exit = True                     
                start()
        except ValueError:   #same as before stops error from other input
            print(f"Error: that is not a vaild option!")
            search_movies()
        except:
            print(f"An error occurred.")
            search_movies()           #just incase there is another error
                     
def rent_movies():   
    user_exit = False                     
    while user_exit == False:   #ask forever until user type finishy
        try:                  
            user_input = str(input("Enter the name of the movie you would like to rent. \nType 'Finish' to return: "))                     
            title = user_input.lower()                     
            title = title.replace(" ", "")        
            print(title)             
            if title != "finish":                     
                if title in set(movies):                     
                    print(f"\nYou have rented {user_input}\n")                     
                    movies.remove(f"{title}")                     #allat just moves it from the available movies to the unavailable ones
                    rented_movies.append(f"{title}")
                    rentcount = rental_keeper.get(title)
                    rentcount += 1   #then counts how many times its been taken out and adds it by one
                    rental_keeper[title] = rentcount
                    reportlist.append(f"{user_input} has been taken out") #then adds it to the logs
                else:                     
                    print(f"\nError: {user_input} is not available or is being rented!\n")                     
            else:                     
                start()                     
                user_exit = True
        except ValueError:
            print(f"Error: that is not a vaild option!")
            rent_movies()
        except:
            print(f"An error occurred.")
            rent_movies()                     
                     
def return_movies():                     
    user_exit = False                     
    while user_exit == False:
        try:
            user_input = str(input("Enter the name of the movie you would like to return. \nType 'Finish' to finish: "))                     
            title = user_input.lower()                     
            title = title.replace(" ", "")                     
            if title != "finish":                     
                if title in set(rented_movies):                     
                    print(f"\nYou have returned {user_input}\n.")       #removes movie from currently rented list to the available library
                    rented_movies.remove(f"{title}")                     
                    movies.append(f"{title}")
                    reportlist.append(f"{user_input} has been returned")          #then adds it to the logs
                else:                     
                    print(f"\nError: {user_input} has not been rented.\n")                     
            else:                     
                start()                     
                user_exit = True    
        except ValueError:
            print(f"Error: that is not a vaild option!")
            return_movies()
        except:
            print(f"An error occurred.")
            return_movies()                 
                     
                     
                     
def admin_menu():                     
    user_exit = False                     
    while user_exit != True:
        try:                     
            print("\n----- Administrative Options ------\n")                     
            user_input = int(input("Choose your option: \n1 - Add Movies\n2 - Remove Movies\n3 - Cost Calculator\n4 - Movies List \n5 - Generate Rental Report\n6 - Main Menu\n\n"))                     
            if user_input == 1:                     
                add_movies()                     
            elif user_input == 2:                     
                remove_movies()                     
            elif user_input == 3:                     
                costcalculate()
            elif user_input == 4:
                movielist()     
            elif user_input == 5:
                generate_rental_report()                
            elif user_input == 6:                     
                start()                     
            else:                     
                print(f"Error: {user_input} is not an option!")                     
                admin_menu()                     
            user_exit = True                     
        except ValueError:
            print(f"Error: that is not a vaild option!")
            admin_menu()
        except:
            print(f"An error occurred.")
            admin_menu()                                 
                     
def add_movies():                     
    user_exit = False                     
    while user_exit != True:  
        try:                   
            user_input = str(input("\nEnter the name of the movie you would like to add to the library.\nType 'Finish' to finish: "))                     
            title = user_input.lower()                     
            title = title.replace(" ","")
            if title != "finish":
                print(f"Added '{user_input}' to the movies list!")                     
                movies.append(title) #adds movie to available library
                rental_keeper.update({title: 0}) #then creates a dictionary for it to say its been rented 0 times
            else:                     
                user_exit = True                     
                admin_menu()
        except ValueError:
            print(f"Error: that is not a vaild option!")
            admin_menu()
        except:
            print(f"An error occurred.")
            admin_menu()                     
                     
def costcalculate():                     
    user_exit = False                     
    while user_exit != True: 
        try:                   
            user_input = str(input("\nEnter the name of the movie you would like to calculate its revenue.\nType 'Finish' to finish: "))
            title = user_input.lower()
            title = title.replace(" ","")
            if title != "finish":
                print(f"{user_input} has been rented {rental_keeper[title]} times!")
                price = int(input("How much does this movie cost? "))
                print(f"{user_input} has made ${rental_keeper[title] * price}!") #gets the amount of times its been taken out then multiplies it by the user input to calculate the maount of money its made
            else:
                user_exit = True
                admin_menu()
        except ValueError:
            print(f"Error: that is not a vaild option!")
            costcalculate()
        except:
            print(f"An error occurred.")
            costcalculate()               
                     
def generate_rental_report():
    print("\n----- Rental List -----\n")
    for i in reportlist:
        print(f"- {i}")  #shows the log
    admin_menu()



def remove_movies():
    user_exit = False                     
    while user_exit != True: 
        try:                    
            user_input = str(input("\nEnter the name of the movie you would like to remove from the library.\nType 'Finish' to finish: "))                     
            title = user_input.lower()                     
            title = title.replace(" ","")                     
            if title != "finish":
                if title in set(movies):
                    movies.remove(f"{title}") #removes the movie from both lists
                elif title in set(rented_movies):
                    rented_movies.remove(f"{title}")
                print(f"Removed '{user_input}' from the movies list!")
            else:
                user_exit = True
                admin_menu()                     
        except ValueError:
            print(f"Error: that is not a vaild option!")
            search_movies()
        except:
            print(f"An error occurred.")
            search_movies()                     

def movielist():
    print("\n----- Movies List -----\n") #shows all of the movies
    print("\n- Unrented Movies: \n")
    place = 0
    for i in movies:
        place += 1
        print(f"{place}. {i}")
    print("\n- Rented Movies: ")
    for i in rented_movies:
        place += 1
        print(f"{place}. {i}")
    user_exit = False
    while user_exit != True:
       user_input = str(input("\nType 'Finish' to go back to the main menu: "))
       user_input.lower()
       if user_input == "finish":
           admin_menu()
           user_exit = True
                     
start()
