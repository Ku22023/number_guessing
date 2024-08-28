movies = {"LOTF": 10,
          "JIANAN": 5,
          "MO": 15,
          "JACKY": 10,
          }
rent_tracker = {"LOTF": 1,
                }
rented_movies = ["LOTF",
                 "JIANAN"
                 ]
available_movies = ["MO",
                    "JACKY"]

def movie_search(user_input):
    for i in movies:
        if i == user_input:
            print(i)
            return True
        else:
            continue

def movie_rent():
    pass

def movie_return():
    pass

menu = True
admin_menu = False
while menu == True:
    print("--- MOVIE THEATRE ---")
    user_input = int(input("Please Select your option:" \
                           "\n1. Search for a Movie" \
                           "\n2. Rent a Movie" \
                           "\n3. Return a Movie" \
                           "\n4. Admin Access" \
                           "\n"))
    if user_input == 1:
        user_input = str(input("Please enter the title of the movie you "\
                               "would like to seach for"))
        movie = movie_search(user_input)
        movie_search()
    elif user_input == 2:
        movie_rent()
    elif user_input == 3:
        movie_return()
    elif user_input == 4:
        admin_menu == True