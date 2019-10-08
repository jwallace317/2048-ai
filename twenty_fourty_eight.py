import random
from board import Board

rows = 4
columns = 4
board_state = [[-1 for column in range(columns)] for row in range(rows)]

# prints the given board state to the screen
def print_board(board):
    for row in range(rows):
        for column in range(columns):
            print('|', end=' ')

            if board[row][column] == -1:
                print('-', end=' ')
            else:
                print(board[row][column], end=' ')

            print('|', end=' ')
        print()


# returns the last open tile moving from the given position in an upwards direction
def detect_up_collision(board, row, column):
    new_row = row
    for i in range(1, rows + 1):
        if row - i >= 0:
            if board[row - i][column] != -1:
                if board[row - i][column] != board[row][column]:
                    new_row = row - i + 1
                else:
                    new_row = row - i
                break
        else:
            new_row = 0
            break

    return new_row, column


def detect_down_collision(board, row, column):
    new_row = row
    for i in range(1, rows + 1):
        if row + i <= 3:
            if board[row + i][column] != board[row][column]:
                new_row = row + i - 1
            else:
                new_row = row + i
                break
        else:
            new_row = 3
            break

    return new_row, column


def detect_right_collision(board, row, column):
    new_column = column
    for i in range(1, columns + 1):
        if column + i <= 3:
            if board[row][column + i] != board[row][column]:
                new_column = column + i - 1
            else:
                new_column = column + i
                break
        else:
            new_column = 3
            break

    return row, new_column


def detect_left_collision(board, row, column):
    new_column = column
    for i in range(1, columns + 1):
        if column - i >= 0:
            if board[row][column - i] != board[row][column]:
                new_column = column - i + 1
            else:
                new_column = column - i
                break
        else:
            new_column = 0

    return row, new_column


def swap_positions(board, row, column, new_row, new_column):
    if row != new_row or column != new_column:
        temp = board[new_row][new_column]
        board[new_row][new_column] = board[row][column]
        board[row][column] = temp
    else:
        board[new_row][new_column] = board[row][column]*2
        board[row][column] = -1

# def move(board, direction):
#     # if direction is up
#     if direction == 'up':
#         for i in range(rows):
#             for j in range(columns):
#                 move_tile(board, i, j, direction)
#     elif direction == 'down':
#         for i in [3, 2, 1, 0]:
#             for j in [3, 2, 1, 0]:
#                 move_tile(board, i, j, direction)
#     elif direction == 'left':
#         for i in [3, 2, 1, 0]:
#             for j in [3, 2, 1, 0]:
#                 move_tile(board, j, i, direction)
#     elif direction == 'right':
#         for i in range(columns):
#             for j in range(rows):
#                 move_tile(board, j, i, direction)

def move(board, direction):
    if direction == 'up':
        for i in range(0, 4):
            for j in range(0, 4):
                if board[i][j] != -1:
                    print(i)
                    print(j)
                    new_row, new_column = detect_up_collision(board, i, j)
                    swap_positions(board, i, j, new_row, new_column)
    elif direction == 'down':
        return 1
    elif direction == 'left':
        return 1
    elif direction == 'right':
        return 1
    else:
        return 1


def move_tile(board, row, column, direction):
    if board[row][column] != -1:
        if direction == 'up':
            new_row, new_column = detect_up_collision(board, row, column)
            swap_positions(board, row, column, new_row, new_column)
        elif direction == 'down':
            new_row, new_column = detect_down_collision(board, row, column)
            swap_positions(board, row, column, new_row, new_column)
        elif direction == 'left':
            new_row, new_column = detect_left_collision(board, row, column)
            swap_positions(board, row, column, new_row, new_column)
        elif direction == 'right':
            new_row, new_column = detect_right_collision(board, row, column)
            swap_positions(board, row, column, new_row, new_column)
        else:
            print('invalid direction given')

    return 1


def is_tile_occupied(board, row, column):
    if board[row][column] == -1:
        return False
    else:
        return True


def insert_tile(board):
    while True:
        row = random.randint(0, 3)
        column = random.randint(0, 3)

        if not is_tile_occupied(board, row, column):
            break

    if random.random() < 0.9:
        board[row][column] = 2
    else:
        board[row][column] = 4

# create a new game
def new_game(board):
    for i in range(rows):
        for j in range(columns):
            board[i][j] = -1

    for i in range(2):

        while True:
            row = random.randint(0, 3)
            column = random.randint(0, 3)

            if not is_tile_occupied(board, row, column):
                break

        if random.random() < 0.9:
            board[row][column] = 2
        else:
            board[row][column] = 4


def main():
    new_game(board_state)

    board = Board()
    board.new_game()
    while True:
        board.print()
        direction = input('direction: ')
        board.move(direction)
        board.insert_random_tile()



if __name__ == '__main__':
    main()