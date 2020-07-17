from random import randint


class Minesweeper:

    def __init__(self, rows=8, columns=8):
        self.board = []
        self.rows = rows
        self.columns = columns
        self.size = self.rows * self.columns
        for _ in range(rows):
            row = []
            for _ in range(columns):
                if randint(0, rows*columns) < self.size / 5:
                    row.append(-1)
                else:
                    row.append(0)
            self.board.append(row)
