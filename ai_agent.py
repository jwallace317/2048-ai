from copy import deepcopy

neighbors = {
    (0, 0): [(0, 1), (1, 0)],
    (0, 1): [(0, 0), (0, 2), (1, 1)],
    (0, 2) : [(0, 1), (0, 3), (1, 2)],
    (0, 3) : [(0, 2), (1, 3)],
    (1, 0) : [(0, 0), (2, 0), (1, 1)],
    (1, 1) : [(1, 0), (1, 2), (0, 1), (2, 1)],
    (1, 2) : [(1, 1), (1, 3), (0, 2), (2, 2)],
    (1, 3) : [(1, 2), (0, 3), (2, 3)],
    (2, 0) : [(2, 1), (1, 0), (3, 0)],
    (2, 1) : [(2, 0), (2, 2), (1, 1), (3, 1)],
    (2, 2) : [(2, 1), (2, 3), (1, 2), (3, 2)],
    (2, 3) : [(2, 2), (1, 3), (3, 3)],
    (3, 0) : [(3, 1), (2, 0)],
    (3, 1) : [(3, 0), (3, 2), (2, 1)],
    (3, 2) : [(3, 1), (3, 3), (2, 2)],
    (3, 3) : [(3, 2), (2, 3)]
}


class AIAgent:

    def __init__(self):
        # the weights matrix
        self.weights = [
            [6, 5, 4, 3],
            [5, 4, 3, 2],
            [4, 3, 2, 1],
            [3, 2, 1, 0]
        ]

    def best_move(self, board, depth, is_player):
        # if max depth has been reached, evaluate board state and return score
        if depth == 0:
            return self.evaluate(board)
        # else the max depth has not been reached and it is the board's turn to randomly place a tile
        elif not is_player:
            score = 0

            for tile in board.empty_tiles:
                board_clone = deepcopy(board)
                board_clone.insert_tile(tile[0], tile[1], 2)
                score += 0.9 * self.best_move(board_clone, depth - 1, True)

                board_clone = deepcopy(board)
                board_clone.insert_tile(tile[0], tile[1], 4)
                score += 0.1 * self.best_move(board_clone, depth - 1, True)

            return score / (2*len(board.empty_tiles) + 1)
        # else the max depth has not been reached and it is the player's turn to place a tile
        elif is_player:
            score = 0

            for direction in ['up', 'down', 'left', 'right']:
                board_clone = deepcopy(board)
                board_clone.move(direction)
                score = max(score, self.best_move(board_clone, depth - 1, False))

            return score

    # weight heuristic function - greater scores for high value tiles clustered in the upper left hand corner
    def weight_heuristic(self, board):
        score = 0
        for row in range(4):
            for column in range(4):
                score += self.weights[row][column] * board.board[row][column]

        return score

    # returns a negative value for clusters of tiles with large differences in value
    def cluster_heuristic(self, board):
        penalty = 0
        for row in range(4):
            for column in range(4):
                for neighbor in neighbors.get((row, column)):
                    penalty += abs(board.board[row][column] - board.board[neighbor[0]][neighbor[1]])

        return penalty

    # for now return the weight heuristic evaluation, will create penalty for poorly clustered tiles
    def evaluate(self, board):
        return self.weight_heuristic(board) - self.cluster_heuristic(board)
