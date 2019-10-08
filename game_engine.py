from board import Board
from util import end_game
from util import evaluate_score


def game():
    board = Board()
    board.new_game()

    while not end_game(board):
        board.print()
        print('score: ' + str(evaluate_score(board)))
        direction = input('direction: ')
        board.move(direction)
        board.insert_random_tile()


if __name__ == '__main__':
    game()
