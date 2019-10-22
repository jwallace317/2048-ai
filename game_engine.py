from board import Board


def game():
    board = Board()
    board.clear()

    while len(board.valid_moves()) > 0:
        board.print()

        direction = input('direction: ')

        if board.valid_move(direction):
            board.move(direction)
            board.insert_random_tile()
        else:
            print('invalid move')


if __name__ == '__main__':
    game()
