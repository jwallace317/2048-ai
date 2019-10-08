from copy import deepcopy
import util


class AIAgent:

    def __init__(self, board):
        self.board = board

    # evaluate the given board
    def evaluate_board(self, board):
        score = 0
        for row in range(self.board.rows):
            for column in range(self.board.columns):
                if board.board[row][column] != -1:
                    score += board.board[row][column]

        return score

    # determine if there are any valid moves left
    # move to util class
    def moves_left(self, board):
        board_copy_up = deepcopy(board)
        board_copy_down = deepcopy(board)
        board_copy_left = deepcopy(board)
        board_copy_right = deepcopy(board)

        board_copy_up.move('up')
        board_copy_down.move('down')
        board_copy_left.move('left')
        board_copy_right.move('right')

        up = util.different_boards(board.board, board_copy_up.board)
        down = util.different_boards(board.board, board_copy_down.board)
        left = util.different_boards(board.board, board_copy_left.board)
        right = util.different_boards(board.board, board_copy_right.board)

        if not up and not down and not left and not right:
            return False
        else:
            return True

    def find_next_best_move(self):
        # start with an up move
        board_copy_up = deepcopy(self.board)

        board_copy_up.move('up')
        while self.moves_left(board_copy_up):
            direction = util.generate_random_move()
            board_copy_up.move(direction)
            board_copy_up.insert_random_tile()

        return self.evaluate_board(board_copy_up)

        # start with a down move
        board_copy_down = deepcopy(self.board)

        # start with a left move
        board_copy_left = deepcopy(self.board)

        # start with a right move
        board_copy_right = deepcopy(self.board)