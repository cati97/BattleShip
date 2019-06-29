from battleship.board import *


class Player:
    def __init__(self, name):
        self.name = name
        self.b_obj = Board()
        self.player_board = self.b_obj.get_new_board()
        self.shooting_board = self.b_obj.get_new_board()

    def get_name(self):  # getter
        return self.name

    def print_board(self, b):
        self.b_obj.print_joined_board(b)

    def print_empty_board(self, b):
        self.b_obj.print_empty_board(b)

