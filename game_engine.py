from board import Board

def main():
    board = Board()
    board.new_game()
    while True:
        board.print()
        direction = input('direction: ')
        board.move(direction)
        board.insert_random_tile()


if __name__ == '__main__':
    main()