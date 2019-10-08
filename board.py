# import necessary modules
import random
from collision_detector import CollisionDetector


# Board class
class Board:

    # initialize the board as a 4x4 matrix filled with -1's to indicate unoccupied tiles
    def __init__(self):
        self.rows = 4
        self.columns = 4
        self.board = [[-1 for column in range(self.columns)] for row in range(self.rows)]
        self.collision_detector = CollisionDetector(self)

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

    # moves a tile in a given direction with the correct collision logic
    def move_tile(self, row, column, direction):
        if direction == 'up':
            new_row = self.collision_detector.detect_up_collision(row, column)

            if self.board[new_row][column] == self.board[row][column] and new_row != row:
                self.board[new_row][column] = 2 * self.board[row][column]
                self.board[row][column] = -1
            elif new_row != row:
                self.board[new_row][column] = self.board[row][column]
                self.board[row][column] = -1

        if direction == 'down':
            new_row = self.collision_detector.detect_down_collision(row, column)

            if self.board[new_row][column] == self.board[row][column] and new_row != row:
                self.board[new_row][column] = 2 * self.board[row][column]
                self.board[row][column] = -1
            elif new_row != row:
                self.board[new_row][column] = self.board[row][column]
                self.board[row][column] = -1

        if direction == 'left':
            new_column = self.collision_detector.detect_left_collision(row, column)

            if self.board[row][new_column] == self.board[row][column] and new_column != column:
                self.board[row][new_column] = 2 * self.board[row][column]
                self.board[row][column] = -1
            elif new_column != column:
                self.board[row][new_column] = self.board[row][column]
                self.board[row][column] = -1

        if direction == 'right':
            new_column = self.collision_detector.detect_right_collision(row, column)

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
