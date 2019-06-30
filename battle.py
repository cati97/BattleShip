
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
        time.sleep(3)
        clear()
        if random1 > random2:
            starts = player1
            break
        elif random1 == random2:
            print("It's a draw! Let's try again")
            time.sleep(2)
            continue
        else:
            starts = player2
            break
    return starts


def choose_amount_ships():
    amount = input("Please choose the amount of ships from 2 to 5: ")
    amount = validate_amount_ships(amount)
    return amount


def return_ships():
    ships = [5, 4, 3, 3, 2, 2]
    amount = choose_amount_ships()
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
        letter = validate_letter(letter)
        number = input("Number: ")
        number = validate_number(number)  # returns a valid number as int
        direction = input("Horizontally(h) or Vertically (v): ")
        # direction = validate_direction(direction)
        clear()
        print("         {}'s board ".format(player.name))
        player.player_board = player.b_obj.return_board_with_ship(letter, number, ship, direction, player.player_board)
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


def shooting(player1, player2, ships):
    shooter = who_starts(player1, player2)
    if shooter == player1:
        enemy = player2
    else:
        enemy = player1
    enemy.stars_remaining = enemy.b_obj.count_stars_total(ships)
    print("{} you start! Give computer to {}".format(shooter.name, shooter.name))
    time.sleep(10)
    clear()
    while enemy.stars_remaining > 0:
        print("{}'s turn\n".format(shooter.name))
        print("             {}".format(shooter.name))
        shooter.print_board(shooter.player_board)
        print("             {}".format(enemy.name))
        enemy.print_board(enemy.shooting_board)
        print("Shoot! ")
        shooting_rules()
        letter = input("Letter: ")
        letter = validate_letter(letter)
        number = input("Number: ")
        number = validate_number(number)
        clear()
        is_there_star = enemy.b_obj.check_for_star_at_coordinates(enemy.player_board, letter, number)
        if is_there_star:
            enemy.shooting_board = enemy.b_obj.place_hit_miss_on_enemy(letter, number,
                                                                       enemy.player_board, enemy.shooting_board)
            enemy.player_board = enemy.b_obj.place_hit_miss_on_yourself(letter, number, enemy.player_board,
                                                                        enemy.shooting_board)
            enemy.stars_remaining -= 1
            continue
        else:
            enemy.shooting_board = enemy.b_obj.place_hit_miss_on_enemy(letter, number,
                                                                       enemy.player_board, enemy.shooting_board)
            enemy.player_board = enemy.b_obj.place_hit_miss_on_yourself(letter, number, enemy.player_board,
                                                                        enemy.shooting_board)

            print("{}'s turn\n".format(shooter.name))
            print("             {}".format(shooter.name))
            shooter.print_board(shooter.player_board)
            print("             {}".format(enemy.name))
            enemy.print_board(enemy.shooting_board)
            time.sleep(2)
            clear()
            print("You missed! Give computer to: {}".format(enemy.name))
            time.sleep(10)
            clear()
            shooter, enemy = enemy, shooter  # swapping two variables
            continue
    print("{} you win!!!".format(shooter.name))


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
            ships = return_ships()
            p1_name = input("Player 1, please enter your name: ")
            p2_name = input("Player 2, please enter your name: ")
            clear()
            p1 = Player(p1_name)
            p2 = Player(p2_name)
            start_game(p1, ships)
            time.sleep(3)
            clear()
            start_game(p2, ships)
            time.sleep(3)
            clear()
            shooting(p1, p2, ships)
            continue
        if user_input == "q":
            print("See you next time! Bye ")
            break
        else:
            print("\nSorry I don't understand")
            print_shortcuts()
            continue


main()
