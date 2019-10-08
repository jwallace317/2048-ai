import random


class Board:

    def __init__(self):
        self.rows = 4
        self.columns = 4
        self.board = [[-1 for column in range(self.columns)] for row in range(self.rows)]

    # prints the board to the terminal
    def print(self):
        for row in range(self.rows):
            for column in range(self.columns):
                print('|', end=' ')

                if self.board[row][column] == -1:
                    print('-', end=' ')
                else:
                    print(self.board[row][column], end=' ')

                print('|', end=' ')
            print()

    # clears the board and inserts two random tiles
    def new_game(self):
        for i in range(self.rows):
            for j in range(self.columns):
                self.board[i][j] = -1

        for i in range(2):
            while True:
                row = random.randint(0, 3)
                column = random.randint(0, 3)

                if not self.is_tile_occupied(row, column):
                    break

            if random.random() < 0.9:
                self.board[row][column] = 2
            else:
                self.board[row][column] = 4

    # checks to see if a tile is occupied at a given position
    def is_tile_occupied(self, row, column):
        if self.board[row][column] == -1:
            return False
        else:
            return True

    def move_tile(self, row, column, direction):
        if direction == 'up':
            new_row = 0
            for i in range(1, self.rows):
                if row - i < self.rows:
                    if self.is_tile_occupied(row - i, column):
                        if self.board[row - i][column] == self.board[row][column]:
                            new_row = row - i
                        else:
                            new_row = row - i + 1
                        break
                    else:
                        new_row = row - i
                else:
                    break

            if self.board[row - i][column] == self.board[row][column] and new_row != row:
                self.board[new_row][column] = 2*self.board[row][column]
                self.board[row][column] = -1
            elif new_row != row:
                self.board[new_row][column] = self.board[row][column]
                self.board[row][column] = -1

        if direction == 'down':
            new_row = 3
            for i in range(1, self.rows):
                if row + i <= self.rows - 1:
                    if self.is_tile_occupied(row + i, column):
                        if self.board[row + i][column] == self.board[row][column]:
                            new_row = row + i
                        else:
                            new_row = row + i - 1
                        break
                    else:
                        new_row = row + i
                else:
                    break

            if self.board[new_row][column] == self.board[row][column] and new_row != row:
                self.board[new_row][column] = 2*self.board[row][column]
                self.board[row][column] = -1
            elif new_row != row:
                self.board[new_row][column] = self.board[row][column]
                self.board[row][column] = -1

        if direction == 'left':
            new_column = 0
            for i in range(1, self.columns):
                if column - i >= 0:
                    if self.is_tile_occupied(row, column - i):
                        if self.board[row][column - i] == self.board[row][column]:
                            new_column = column - i
                        else:
                            new_column = column - i + 1
                        break
                    else:
                        new_column = column - i
                else:
                    break

            if self.board[row][new_column] == self.board[row][column] and new_column != column:
                self.board[row][new_column] = 2*self.board[row][column]
                self.board[row][column] = -1
            elif new_column != column:
                self.board[row][new_column] = self.board[row][column]
                self.board[row][column] = -1

        if direction == 'right':
            new_column = 3
            for i in range(1, self.columns):
                if column + i <= self.columns - 1:
                    if self.is_tile_occupied(row, column + i):
                        if self.board[row][column + i] == self.board[row][column]:
                            new_column = column + i
                        else:
                            new_column = column + i - 1
                        break
                    else:
                        new_column = column + i
                else:
                    break

            if self.board[row][new_column] == self.board[row][column] and new_column != column:
                self.board[row][new_column] = 2*self.board[row][column]
                self.board[row][column] = -1
            elif new_column != column:
                self.board[row][new_column] = self.board[row][column]
                self.board[row][column] = -1

    def move(self, direction):
        if direction == 'up':
            for row in range(self.rows):
                for column in range(self.columns):
                    if self.is_tile_occupied(row, column):
                        self.move_tile(row, column, direction)
        elif direction == 'down':
            for row in range(self.rows - 1, -1, -1):
                for column in range(self.columns):
                    if self.is_tile_occupied(row, column):
                        self.move_tile(row, column, direction)
        elif direction == 'left':
            for column in range(self.columns):
                for row in range(self.rows):
                    if self.is_tile_occupied(row, column):
                        self.move_tile(row, column, direction)
        elif direction == 'right':
            for column in range(self.columns - 1, -1, -1):
                for row in range(self.rows):
                    if self.is_tile_occupied(row, column):
                        self.move_tile(row, column, direction)

    def insert_random_tile(self):
        while True:
            row = random.randint(0, self.rows - 1)
            column = random.randint(0, self.columns - 1)

            if not self.is_tile_occupied(row, column):
                break

        if random.random() < 0.9:
            self.board[row][column] = 2
        else:
            self.board[row][column] = 4
