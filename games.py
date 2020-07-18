from random import randint


class Minesweeper:

    def __init__(self, rows=8, columns=8, mines=12):
        self.board = []
        self.rows = rows
        self.columns = columns
        self.mines = mines
        self.size = self.rows * self.columns

        mines_position = []
        while len(mines_position) < self.mines:
            x, y = randint(0, self.columns-1), randint(0, self.rows-1)
            if (x, y) not in mines_position:
                mines_position.append((x, y))

        for _ in range(self.rows):
            row = []
            for _ in range(self.columns):
                row.append(0)
            self.board.append(row)

        # record the mines into the board
        for x, y in mines_position:
            self.board[y][x] = -1

        # compute and record cells surrounding mines
        for x, y in mines_position:
            for dy in (-1, 0, 1):
                for dx in (-1, 0, 1):
                    if 0 <= x+dx < self.rows and 0 <= y+dy < self.columns:
                        if self.board[y+dy][x+dx] != -1:
                            self.board[y+dy][x+dx] += 1

    def get_user_board(self):
        return self.board
