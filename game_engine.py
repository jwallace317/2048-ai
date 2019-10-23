from copy import deepcopy

from ai_agent import AIAgent
from board import Board


def game():
    board = Board()
    board.new_game()

    ai_agent = AIAgent()

    while len(board.valid_moves()) > 0:
        board.print()

        best_move = None
        max_score = 0
        for direction in ['up', 'down', 'left', 'right']:
            board_clone = deepcopy(board)
            board_clone.move(direction)
            score = ai_agent.best_move(board_clone, 3, False)

            if board.valid_move(direction):
                if score > max_score:
                    best_move = direction
                    max_score = score
                elif best_move is None:
                    best_move = direction

        print('best direction to move: ' + best_move)

        direction = best_move

        board.move(direction)
        board.insert_random_tile()


if __name__ == '__main__':
    game()
