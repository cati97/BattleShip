class Board:

    r0 = ["║  ", " ║ ", "A", " ║ ", "B", " ║ ", "C", " ║ ", "D", " ║ ", "E", " ║ ", "F", " ║ ", "G", " ║"]
    r1 = ["║ 1", " ║ ", " ", " ║ ", " ", " ║ ", " ", " ║ ", " ", " ║ ", " ", " ║ ", " ", " ║ ", " ", " ║"]
    r2 = ["║ 2", " ║ ", " ", " ║ ", " ", " ║ ", " ", " ║ ", " ", " ║ ", " ", " ║ ", " ", " ║ ", " ", " ║"]
    r3 = ["║ 3", " ║ ", " ", " ║ ", " ", " ║ ", " ", " ║ ", " ", " ║ ", " ", " ║ ", " ", " ║ ", " ", " ║"]
    r4 = ["║ 4", " ║ ", " ", " ║ ", " ", " ║ ", " ", " ║ ", " ", " ║ ", " ", " ║ ", " ", " ║ ", " ", " ║"]
    r5 = ["║ 5", " ║ ", " ", " ║ ", " ", " ║ ", " ", " ║ ", " ", " ║ ", " ", " ║ ", " ", " ║ ", " ", " ║"]
    r6 = ["║ 6", " ║ ", " ", " ║ ", " ", " ║ ", " ", " ║ ", " ", " ║ ", " ", " ║ ", " ", " ║ ", " ", " ║"]
    r7 = ["║ 7", " ║ ", " ", " ║ ", " ", " ║ ", " ", " ║ ", " ", " ║ ", " ", " ║ ", " ", " ║ ", " ", " ║"]

    board = [r0, r1, r2, r3, r4, r5, r6, r7]

    beginning = "╔═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╗"

    between = "╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣"

    ending = "╚═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╝"

    letters = {
        "A": 2,
        "B": 4,
        "C": 6,
        "D": 8,
        "E": 10,
        "F": 12,
        "G": 14
    }

    def get_new_board(self):
        new_board = [row[:]for row in self.board]
        return new_board

    def return_board_with_ship(self, letter, number, ship, direction, players_board):  # A 1
        letter = letter.upper()
        letter_as_num = self.letters.get(letter)
        if direction == "h":
            for i in range(ship):
                players_board[number][letter_as_num] = '*'
                letter_as_num += 2
            return players_board

        if direction == "v":
            for i in range(ship):
                players_board[number][self.letters.get(letter)] = '*'
                number += 1
            return players_board

    def print_joined_row(self, row):
        row_joined = ""
        for element in row:
            row_joined += element
        print(row_joined)

    def print_joined_board(self, b):
        if isinstance(b, list):  # if object is a list
            print(self.beginning)
            for i in range(len(b)):
                self.print_joined_row(b[i])
                if i < (len(b) - 1):
                    print(self.between)
            print(self.ending)

    def print_empty_board(self, board):
        if isinstance(board, list):
            for row in board:
                for element in row:
                    if row == board[0]:
                        continue
                    else:
                        if row.index(element) % 2 == 0 and row.index(element) != 0:
                            board[board.index(row)][row.index(element)] = " "
            self.print_joined_board(board)

    def check_for_star_at_coordinates(self, board, letter, number):
        letter = letter.upper()
        if isinstance(board, list):
            letter_as_num = self.letters.get(letter)
            if board[number][letter_as_num] == "*":
                return True
            else:
                return False


    def place_hit_miss_on_enemy(self, letter, number, real_board, shooting_board):
        letter = letter.upper()
        if isinstance(real_board, list) and isinstance(shooting_board, list):
            letter_as_num = self.letters.get(letter)
            if real_board[number][letter_as_num] == "*":
                shooting_board[number][letter_as_num] = "X"
                return shooting_board
            elif real_board[number][letter_as_num] == " ":
                shooting_board[number][letter_as_num] = "~"
                return shooting_board

    def place_hit_miss_on_yourself(self, letter, number, real_board, shooting_board):
        letter = letter.upper()
        if isinstance(real_board, list) and isinstance(shooting_board, list):
            letter_as_num = self.letters.get(letter)
            if shooting_board[number][letter_as_num] == "X":
                real_board[number][letter_as_num] = "X"
                return real_board
            elif shooting_board[number][letter_as_num] == "~":
                real_board[number][letter_as_num] = "~"
                return real_board

    def count_stars_total(self, ships):
        stars = 0
        if isinstance(ships, list):
            for element in ships:
                stars += int(element)
        return stars

    def update_remaining_stars(self, board, count):
        if isinstance(board, list):
            for row in board:
                for element in row:
                    if element == "*":
                        count += 1
        return count
