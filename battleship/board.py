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

    def print_board_with_ship(self, letter, number, ship, h_v):  # A 1
        num = int(number)
        letter_as_num = self.letters.get(letter)
        if h_v == "h":
            for i in range(ship):
                self.board[num][letter_as_num] = '*'
                letter_as_num += 2
            self.print_joined_board(self.board)

        if h_v == "v":
            for i in range(ship):
                self.board[num][self.letters.get(letter)] = '*'
                num += 1
            self.print_joined_board(self.board)


    def print_joined_row(self, row):
        row_joined = ""
        for element in row:
            row_joined += element
        print(row_joined)

    def print_joined_board(self, b):
        print(self.beginning)
        for i in range(len(b)):
            self.print_joined_row(b[i])
            if i < (len(b) - 1):
                print(self.between)
        print(self.ending)

    def print_empty_board(self):
        for row in self.board:
            for element in row:
                if row == self.board[0]:
                    continue
                else:
                    if row.index(element) % 2 == 0 and row.index(element) != 0:
                        self.board[self.board.index(row)][row.index(element)] = " "
        self.print_joined_board(self.board)
