from copy import deepcopy

from ai_agent import AIAgent
from board import Board


def game():
    board = Board()

    for i in range(2):
        board.insert_random_tile()

    board.print()

    ai_agent = AIAgent()

    while len(board.valid_moves()) > 0:
        board.print()

        max_score = 0
        for direction in ['up', 'down', 'left', 'right']:
            board_clone = deepcopy(board)
            board_clone.move(direction)
            score = ai_agent.best_move(board_clone, 3, False)

            if score > max_score and board.valid_move(direction):
                best_move = direction
                max_score = score

        print('best direction to move: ' + best_move)

        direction = best_move

        if board.valid_move(direction):
            board.move(direction)
            board.insert_random_tile()
        else:
            print('invalid move')


if __name__ == '__main__':
    game()
