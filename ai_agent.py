from copy import deepcopy
import util


class AIAgent:

    def __init__(self, board):
        self.board = board

    # evaluate the given board
    def evaluate_board(self):
        score = 0
        for row in range(self.board.rows):
            for column in range(self.board.columns):
                if self.board.board[row][column] != -1:
                    score += self.board.board[row][column]

        return score

    # determine if there are any valid moves left
    def moves_left(self):
        # make a copy of the board
        board_copy_up = deepcopy(self.board)
        board_copy_down = deepcopy(self.board)
        board_copy_left = deepcopy(self.board)
        board_copy_right = deepcopy(self.board)

        board_copy_up.move('up')
        board_copy_down.move('down')
        board_copy_left.move('left')
        board_copy_right.move('right')

        up = util.different_boards(self.board.board, board_copy_up.board)
        down = util.different_boards(self.board.board, board_copy_down.board)
        left = util.different_boards(self.board.board, board_copy_left.board)
        right = util.different_boards(self.board.board, board_copy_right.board)

        if not up and not down and not left and not right:
            return False
        else:
            return True

        # determine if that changed the board state
        # if it did not change the board state at all
        # then that direction is not a valid move
