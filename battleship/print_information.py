

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

Each player has to choose the amount of ships from 2 to 5. 


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


def shooting_rules():
    print("""
    X - hit
    ~ - miss
    """)