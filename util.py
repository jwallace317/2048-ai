# import necessary modules
import random

from copy import deepcopy


# determines whether a given move is valid or not, aka it changes the board state
def valid_move(board, direction):
    board_copy = deepcopy(board)

    board_copy.move(direction)
    if different_boards(board.board, board_copy.board):
        return True
    else:
        return False


# compares two board states to determine if there is a difference or not
def different_boards(antecedent_board, consequent_board):
    for row in range(4):
        for column in range(4):
            if antecedent_board[row][column] != consequent_board[row][column]:
                return True

    return False


# evaluates the score of the board
def evaluate_score(board):
    score = 0
    for row in range(board.rows):
        for column in range(board.columns):
            if board.board[row][column] != -1:
                score += board.board[row][column]

    return score


# determines whether to end the game or not
def end_game(board):
    # if there are no valid moves left, the game is over
    count = 0
    for direction in ['up', 'down', 'left', 'right']:
        board_copy = deepcopy(board)
        if valid_move(board_copy, direction):
            break
        count += 1

    if count == 4:
        return True
    else:
        return False
