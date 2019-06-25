# only the main function

import os  # for os.system("clear") - clearing the screen

import time # time.sleep(10) - number of seconds blocks the program

from battleship.print_information import *

# -------------------- USEFUL FUNCTIONS -----------------


def clear():
    os.system('clear')  # works only when run in the terminal


# ------------------- START GAME ------------------------


class Player:
    def __init__(self, name):
        self.name = name

    def get_name(self):  # getter
        return self.name


def ship_placing(player):
    ships = [5, 4]  # [5, 4, 3, 3, 2, 2] - for real game
    board_p1 = Board()
    print("         {}'s board ".format(player.name))
    board_p1.print_empty_board()
    for ship in ships:
        print("Ship ({}) ".format((ship * '*')))
        letter = input("Letter: ")
        number = input("Number: ")
        h_v = input("Horizontally(h) or Vertically (v): ")
        clear()
        print("         {}'s board ".format(player.name))
        board_p1.print_board_with_ship(letter, number, ship, h_v)


def start_game(player):
    print("\n")
    print("Hello {}, these are your ships: ".format(player.name))
    print("""
1x *****
1x ****
2x ***
2x **  

Please place them on the board.
    """)
    print("""
eg - see example
c - continue
q - return to menu 

""")
    while True:
        user = input(">> ")
        if user == "eg":
            example_placing_ships()
        if user == "c":
            clear()
            ship_placing(player)
            break
        if user == "q":
            break


def main():
    welcome()
    print_shortcuts()
    while True:
        user_input = input("> ")
        if user_input == "r":
            print_rules()
            continue
        if user_input == "s":
            clear()
            p1_name = input("Player 1, please enter your name: ")
            p1 = Player(p1_name)
            start_game(p1)
            time.sleep(3)
            clear()
            p2_name = input("Player 2, please enter your name: ")
            p2 = Player(p2_name)
            start_game(p2)
            continue
        if user_input == "q":
            print("See you next time! Bye ")
            break
        else:
            print("Sorry I don't understand")
            print_shortcuts()
            continue


main()
