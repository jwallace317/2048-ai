import random


def different_boards(antecedent_board, consequent_board):
    for row in range(4):
        for column in range(4):
            if antecedent_board[row][column] != consequent_board[row][column]:
                return True

    return False


def generate_random_move():
    rand = random.randint(1, 4)

    if rand == 1:
        return 'up'
    elif rand == 2:
        return 'down'
    elif rand == 3:
        return 'left'
    elif rand == 4:
        return 'right'
