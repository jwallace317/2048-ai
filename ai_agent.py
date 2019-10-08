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
        up_score_sum = 0
        for i in range(10):
            board_copy_up = deepcopy(self.board)
            board_copy_up.move('up')
            while self.moves_left(board_copy_up):
                direction = util.generate_random_move(board_copy_up)
                board_copy_up.move(direction)
                board_copy_up.insert_random_tile()

            up_score_sum += self.evaluate_board(board_copy_up)

        up_average = up_score_sum / 10

        # start with a down move
        down_score_sum = 0
        for i in range(10):
            board_copy_down = deepcopy(self.board)
            board_copy_down.move('down')
            while self.moves_left(board_copy_down):
                direction = util.generate_random_move(board_copy_down)
                board_copy_down.move(direction)
                board_copy_down.insert_random_tile()

            down_score_sum += self.evaluate_board(board_copy_down)

        down_average = down_score_sum / 10

        # start with a left move
        left_score_sum = 0
        for i in range(10):
            board_copy_left = deepcopy(self.board)
            board_copy_left.move('left')
            while self.moves_left(board_copy_left):
                direction = util.generate_random_move(board_copy_left)
                board_copy_left.move(direction)
                board_copy_left.insert_random_tile()

            left_score_sum += self.evaluate_board(board_copy_left)

        left_average = left_score_sum / 10

        # start with a right move
        right_score_sum = 0
        for i in range(10):
            board_copy_right = deepcopy(self.board)
            board_copy_right.move('right')
            while self.moves_left(board_copy_right):
                direction = util.generate_random_move(board_copy_right)
                board_copy_right.move(direction)
                board_copy_right.insert_random_tile()

            right_score_sum += self.evaluate_board(board_copy_right)

        right_average = right_score_sum / 10

        print('up average: ' + str(up_average) + ' valid move: ' + str(util.valid_move(self.board, 'up')))
        print('down average: ' + str(down_average) + ' valid move: ' + str(util.valid_move(self.board, 'down')))
        print('left average: ' + str(left_average) + ' valid move: ' + str(util.valid_move(self.board, 'left')))
        print('right average: ' + str(right_average) + ' valid move: ' + str(util.valid_move(self.board, 'right')))

        max_average = max([up_average, down_average, left_average, right_average])

        if max_average == up_average:
            return 'up'
        elif max_average == down_average:
            return 'down'
        elif max_average == left_average:
            return 'left'
        elif max_average == right_average:
            return 'right'