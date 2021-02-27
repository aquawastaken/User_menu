MENU_PROMPT = "\nEnter 'a' to enter a new movie 's' to look up a movie youve added 'l' to list all the movies you have now: "

movies = []

def add_movie():
    title = input("Enter movie title: ")
    year = input("Enter the year the movie was added: ")
    director = input("Enter the director of the movie: ")

    movies.append({
        "title": title,
        "year": year,
        "director": director
    })

def list_movie():
    amount_of_movies = len(movie)
    print(f"You currently have about {amount_of_movies}")
    user_response = input("would you like to see them?: ")
    if user_response == 'yes':
        print("listing movies...")
        print(movie)
        print("All done :D")
    elif user_response  == 'No':
        print("Understood restarting program.")
    else:
        print('Invalid input')

def movie_search():
    user_question = input("please enter the movie that you'd like to find: ")
    for movie in movies:
        if user_question == movie['title']:
            print("We found your movie!")
            print(movie)
        else:
            print("Sorry its not here")

def menu_start():
    selection = input(MENU_PROMPT)
    while selection:
        if selection == "a":
            add_movie()
            print("succesfully added")

        elif selection == "l":
            list_movie()

        elif selection == "s":
            movie_search()

        else:
            print('Invalid input')

        selection = input(MENU_PROMPT)


menu_start()