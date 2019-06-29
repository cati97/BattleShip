
import time  # time.sleep(10) - number of seconds blocks the program

from battleship.print_information import *

from battleship.useful import *

from battleship.player import *

import random


def roll_dice():
    return random.randint(1, 6)


def who_starts(player1, player2):
    print("Let's roll a dice to see who starts the game")
    starts = Player("")
    while True:
        input("{} press enter to roll: ".format(player1.name))
        random1 = roll_dice()
        print(random1)
        input("{} press enter to roll: ".format(player2.name))
        random2 = roll_dice()
        print(random2)
        if random1 > random2:
            starts = player1
            break
        elif random1 == random2:
            continue
        else:
            starts = player2
            break
    return starts


def choose_amount_ships():
    ships = [5, 4, 3, 3, 2, 2]
    amount = int(input("Please choose the amount of ships from 2 to 5: "))
    clear()
    for x in range(2, 6):
        if x == amount:
            ships = ships[:x]
        else:
            continue
    return ships


def ship_placing(player, ships):
    print("         {}'s board ".format(player.name))
    player.print_board(player.player_board)  # prints empty board
    for ship in ships:
        print("Ship ({}) ".format((ship * '*')))
        letter = input("Letter: ")
        number = input("Number: ")
        h_v = input("Horizontally(h) or Vertically (v): ")
        clear()
        print("         {}'s board ".format(player.name))
        player.player_board = player.b_obj.return_board_with_ship(letter, number, ship, h_v, player.player_board)
        player.b_obj.print_joined_board(player.player_board)


def start_game(player, ships):
    print("\nHello {}, ".format(player.name))

    print("""
c - continue
q - return to main menu 

""")
    while True:
        user = input(">> ")
        if user == "c":
            clear()
            ship_placing(player, ships)
            break
        if user == "q":
            break


def shooting(player1, player2):
    shooter = player1
    enemy = player2
    while True:
        print("{}'s turn".format(shooter.name))
        print("Your board")
        shooter.print_board(shooter.player_board)
        print("{}'s board".format(enemy.name))
        enemy.print_board(enemy.shooting_board)
        print("Shoot! ")
        shooting_rules()
        letter = input("Letter: ")
        number = input("Number: ")
        clear()
        is_there_star = enemy.b_obj.check_for_star(enemy.player_board, letter, number)
        if is_there_star:
            enemy.shooting_board = enemy.b_obj.place_hit_miss(letter, number, enemy.player_board, enemy.shooting_board)
            shooter = player1
            enemy = player2
            continue
        else:
            enemy.shooting_board = enemy.b_obj.place_hit_miss(letter, number, enemy.player_board, enemy.shooting_board)
            shooter = player2
            enemy = player1
            continue


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
            ships = choose_amount_ships()
            p1_name = input("Player 1, please enter your name: ")
            p2_name = input("Player 2, please enter your name: ")
            clear()
            p1 = Player(p1_name)
            p2 = Player(p2_name)
            start_game(p1, ships)
            time.sleep(3)
            # how to get to data - > p1.print_board(p1.player_board)
            clear()
            start_game(p2, ships)
            time.sleep(3)
            clear()
            # starting_player = who_starts(p1, p2)
            # print("{} , you start shooting! ".format(starting_player.name))
            shooting(p1, p2)
            continue
        if user_input == "q":
            print("See you next time! Bye ")
            break
        else:
            print("Sorry I don't understand")
            print_shortcuts()
            continue


main()
