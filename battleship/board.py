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

    def return_board_with_ship(self, letter, number, ship, h_v, players_board):  # A 1
        num = int(number)
        letter_as_num = self.letters.get(letter)
        if h_v == "h":
            for i in range(ship):
                players_board[num][letter_as_num] = '*'
                letter_as_num += 2
            return players_board

        if h_v == "v":
            for i in range(ship):
                players_board[num][self.letters.get(letter)] = '*'
                num += 1
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

    def check_for_star(self, board, letter, number):
        if isinstance(board, list):
            num = int(number)
            letter_as_num = self.letters.get(letter)
            if board[num][letter_as_num] == "*":
                return True
            else:
                return False

    def place_hit_miss(self, letter, number, real_board, shooting_board):
        if isinstance(real_board, list) and isinstance(shooting_board, list):
            num = int(number)
            letter_as_num = self.letters.get(letter)
            if real_board[num][letter_as_num] == "*":
                shooting_board[num][letter_as_num] = "X"
                return shooting_board
            elif real_board[num][letter_as_num] == " ":
                shooting_board[num][letter_as_num] = "~"
                return shooting_board
