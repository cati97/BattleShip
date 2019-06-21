def welcome():
    print("\nWelcome in BattleShip")


def show_options_do_chosen():
    choice = input("""
r - see rules
s - start game
q - quit game

Your choice: """)
    while choice in {"r", "s", "q"}:
        if choice == "r":
            print("The rules are... ")
            break
        if choice == "s":
            print("Game starting...")
            break
        if choice == "q":
            print("Bye")
            break
    else:
        print("Sorry, I don't understand you")


welcome()
show_options_do_chosen()







