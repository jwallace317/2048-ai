import random

rows = 4
columns = 4
board_state = [[-1 for i in range(columns)] for j in range(rows)]

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
        if board[row][column] == board[new_row][new_column]:
            board[new_row][new_column] = board[row][column]*2
            board[row][column] = -1
        else:
            board[new_row][new_column] = board[row][column]
            board[row][column] = -1


def move_tile(board, row, column, direction):
    if direction == 'up':
        new_row, new_column = detect_up_collision(board, row, column)
        swap_positions(board, row, column, new_row, new_column)
    elif direction == 'down':
        new_row, new_column = detect_down_collision(board, row, column)
        swap_positions(board, row, column, new_row, new_column)
    elif direction == 'left':
        new_row, new_column = detect_left_collision(board, row, column)
        print(new_row)
        print(new_column)
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

    while True:
        print_board(board_state)
        row = int(input('row '))
        column = int(input('column '))
        direction = input('direction ')
        move_tile(board_state, row, column, direction)
        insert_tile(board_state)


if __name__ == '__main__':
    main()