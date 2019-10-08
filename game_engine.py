from board import Board
from ai_agent import AIAgent

def main():
    board = Board()
    board.new_game()

    ai_agent = AIAgent(board)
    while True:
        board.print()
        print('score: ' + str(ai_agent.evaluate_board(board)))
        print(ai_agent.find_next_best_move())
        direction = input('direction: ')
        board.move(direction)
        board.insert_random_tile()


if __name__ == '__main__':
    main()
