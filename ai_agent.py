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
