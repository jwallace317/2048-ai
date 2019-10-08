# import necessary modules
import random


# Board class
class Board:

    # initialize the board as a 4x4 matrix filled with -1's to indicate unoccupied tiles
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

    # clear the board
    def clear(self):
        for row in range(self.rows):
            for column in range(self.columns):
                self.board[row][column] = -1

    # insert a random 2 tile or a 4 tile on any unoccupied tile of the boardS
    def insert_random_tile(self):
        while True:
            row = random.randint(0, self.rows - 1)
            column = random.randint(0, self.columns - 1)

            if not self.is_tile_occupied(row, column):
                break

        # 90% chance of inserting a 2 tile, 10% chance of inserting a 4 tile
        if random.random() < 0.9:
            self.board[row][column] = 2
        else:
            self.board[row][column] = 4

    # clears the board and inserts two random tiles
    def new_game(self):
        self.clear()

        for i in range(2):
            self.insert_random_tile()

    # checks to see if a tile is occupied at a given position
    def is_tile_occupied(self, row, column):
        if self.board[row][column] == -1:
            return False
        else:
            return True

    # detects the first up collision given the position of a tile and determines how to respond to that collision
    def detect_up_collision(self, row, column):
        new_row = 0
        for i in range(1, self.rows):
            if row - i >= 0:
                if self.is_tile_occupied(row - i, column):
                    if self.board[row - i][column] == self.board[row][column]:
                        new_row = row - i
                    else:
                        new_row = row - i + 1
                    break
            else:
                break

        return new_row

    # detects the first down collision given the position of a tile and determines how to respond to that collision
    def detect_down_collision(self, row, column):
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
                break

        return new_row

    # detects the first left collision given the position of a tile and determines how to respond to that collision
    def detect_left_collision(self, row, column):
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
                break

        return new_column

    # detects the first right collision given the position of a tile and determines how to respond to that collision
    def detect_right_collision(self, row, column):
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
                break

        return new_column

    # moves a tile in a given direction with the correct collision logic
    def move_tile(self, row, column, direction):
        if direction == 'up':
            new_row = self.detect_up_collision(row, column)

            if self.board[new_row][column] == self.board[row][column] and new_row != row:
                self.board[new_row][column] = 2 * self.board[row][column]
                self.board[row][column] = -1
            elif new_row != row:
                self.board[new_row][column] = self.board[row][column]
                self.board[row][column] = -1

        if direction == 'down':
            new_row = self.detect_down_collision(row, column)

            if self.board[new_row][column] == self.board[row][column] and new_row != row:
                self.board[new_row][column] = 2 * self.board[row][column]
                self.board[row][column] = -1
            elif new_row != row:
                self.board[new_row][column] = self.board[row][column]
                self.board[row][column] = -1

        if direction == 'left':
            new_column = self.detect_left_collision(row, column)

            if self.board[row][new_column] == self.board[row][column] and new_column != column:
                self.board[row][new_column] = 2 * self.board[row][column]
                self.board[row][column] = -1
            elif new_column != column:
                self.board[row][new_column] = self.board[row][column]
                self.board[row][column] = -1

        if direction == 'right':
            new_column = self.detect_right_collision(row, column)

            if self.board[row][new_column] == self.board[row][column] and new_column != column:
                self.board[row][new_column] = 2 * self.board[row][column]
                self.board[row][column] = -1
            elif new_column != column:
                self.board[row][new_column] = self.board[row][column]
                self.board[row][column] = -1

    # moves the tiles of the board in a given direction with the correct collision logic
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
