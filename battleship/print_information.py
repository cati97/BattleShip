from battleship.board import *


def welcome():
    print("\nWelcome in BattleShip")


def print_shortcuts():
    print("""
r - see rules
s - start game
q - quit game
""")


def print_rules():
    print("""
------------------BattleShip Game Rules-------------------

Each player has 6 ships:
1x *****
1x ****
2x ***
2x **

Ship placing: 
Players have to place the ships on the board horizontally or vertically.

Game:
Both players throw a dice and the player with bigger number starts.

Player1 starts shooting by guessing coordinates, eg. Shoot: A3. 

Hitting:
If he hit enemy's ship, he shoots again until he misses. 

Missing:
If he misses, it's player2 turn.

Winning:
Player1 wins if Player2 has no ships left. 

s - start game
q - quit game

    """)


def example_placing_ships():
    print("         Player's board ")
    b_example = Board()
    b_example.print_board_with_ship("A", 1, 5, "v")
    print("""
Ship (*****)
Letter: A
Number: 1
Horizontally(h) or Vertically (v): v
    """)