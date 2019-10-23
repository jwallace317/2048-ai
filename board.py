# import necessary modules
import random
from collision_detector import CollisionDetector
from copy import deepcopy


# Board class
class Board:

    # initialize the board as a 4x4 matrix filled with 0's to indicate unoccupied tiles
    def __init__(self):
        self.score = 0
        self.rows = 4
        self.columns = 4
        self.empty_tiles = []
        self.board = [[0 for column in range(self.columns)] for row in range(self.rows)]
        self.collision_detector = CollisionDetector(self)

    # prints the board to the terminal
    def print(self):
        for row in range(self.rows):
            for column in range(self.columns):
                print('|', end=' ')

                if self.board[row][column] == 0:
                    print('-', end=' ')
                else:
                    print(self.board[row][column], end=' ')

                print('|', end=' ')
            print()

        print('score: ' + str(self.score))

    # clear the board
    def clear(self):
        for row in range(self.rows):
            for column in range(self.columns):
                self.board[row][column] = 0
                self.empty_tiles.append((row, column))

    # determines if the board is completely filled with tiles
    def is_board_full(self):
        if len(self.empty_tiles) == 0:
            return True
        else:
            return False

    # insert a tile into a position on the board
    def insert_tile(self, row, column, tile):
        if not self.is_tile_occupied(row, column):
            self.board[row][column] = tile
            self.empty_tiles.remove((row, column))
        else:
            print('tile is occupied')

    # insert a random 2 tile or a 4 tile on any unoccupied tile of the boardS
    def insert_random_tile(self):
        if not self.is_board_full():
            tile = self.empty_tiles[random.randint(0, len(self.empty_tiles) - 1)]

            # 90% chance of inserting a 2 tile, 10% chance of inserting a 4 tile
            if random.random() < 0.9:
                self.insert_tile(tile[0], tile[1], 2)
            else:
                self.insert_tile(tile[0], tile[1], 4)

    # clears the board and inserts two random tiles
    def new_game(self):
        self.score = 0
        self.clear()

        for i in range(2):
            self.insert_random_tile()

    # checks to see if a tile is occupied at a given position
    def is_tile_occupied(self, row, column):
        if self.board[row][column] == 0:
            return False
        else:
            return True

    # moves a tile in a given direction with the correct collision logic
    def move_tile(self, row, column, direction):
        if direction == 'up':
            new_row = self.collision_detector.detect_up_collision(row, column)

            if self.board[new_row][column] == self.board[row][column] and new_row != row:
                self.score += 2 * self.board[row][column]
                self.board[new_row][column] = 2 * self.board[row][column]
                self.board[row][column] = 0
                self.empty_tiles.append((row, column))
            elif new_row != row:
                self.board[new_row][column] = self.board[row][column]
                self.board[row][column] = 0
                self.empty_tiles.append((row, column))
                self.empty_tiles.remove((new_row, column))

        if direction == 'down':
            new_row = self.collision_detector.detect_down_collision(row, column)

            if self.board[new_row][column] == self.board[row][column] and new_row != row:
                self.score += 2 * self.board[row][column]
                self.board[new_row][column] = 2 * self.board[row][column]
                self.board[row][column] = 0
                self.empty_tiles.append((row, column))
            elif new_row != row:
                self.board[new_row][column] = self.board[row][column]
                self.board[row][column] = 0
                self.empty_tiles.append((row, column))
                self.empty_tiles.remove((new_row, column))

        if direction == 'left':
            new_column = self.collision_detector.detect_left_collision(row, column)

            if self.board[row][new_column] == self.board[row][column] and new_column != column:
                self.score += 2 * self.board[row][column]
                self.board[row][new_column] = 2 * self.board[row][column]
                self.board[row][column] = 0
                self.empty_tiles.append((row, column))
            elif new_column != column:
                self.board[row][new_column] = self.board[row][column]
                self.board[row][column] = 0
                self.empty_tiles.append((row, column))
                self.empty_tiles.remove((row, new_column))

        if direction == 'right':
            new_column = self.collision_detector.detect_right_collision(row, column)

            if self.board[row][new_column] == self.board[row][column] and new_column != column:
                self.score += 2 * self.board[row][column]
                self.board[row][new_column] = 2 * self.board[row][column]
                self.board[row][column] = 0
                self.empty_tiles.append((row, column))
            elif new_column != column:
                self.board[row][new_column] = self.board[row][column]
                self.board[row][column] = 0
                self.empty_tiles.append((row, column))
                self.empty_tiles.remove((row, new_column))

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

    # determines whether a given move is valid or not, aka it changes the board state
    def valid_move(self, direction):
        board_copy = deepcopy(self)

        board_copy.move(direction)
        if self.different_boards(board_copy):
            return True
        else:
            return False

    # compares two board states to determine if there is a difference or not
    def different_boards(self, board):
        for row in range(self.rows):
            for column in range(self.columns):
                if self.board[row][column] != board.board[row][column]:
                    return True

        return False

    # returns a list of the valid moves given the current board state
    def valid_moves(self):
        valid_moves = []
        for direction in ['up', 'down', 'left', 'right']:
            board_copy = deepcopy(self)
            if board_copy.valid_move(direction):
                valid_moves.append(direction)

        return valid_moves

    # manually sets the tile of the board
    def set_board(self):
        for row in range(self.rows):
            for column in range(self.columns):
                tile = int(input(''))
                self.board[row][column] = tile

    def clone(self):
        return deepcopy(self)
