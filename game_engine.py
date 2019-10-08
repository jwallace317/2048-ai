from board import Board
from ai_agent import AIAgent

def main():
    board = Board()
    board.new_game()

    ai_agent = AIAgent(board)
    while True:
        board.print()
        print('score: ' + str(ai_agent.evaluate_board()))
        print(ai_agent.moves_left())
        direction = input('direction: ')
        board.move(direction)
        board.insert_random_tile()


if __name__ == '__main__':
    main()
