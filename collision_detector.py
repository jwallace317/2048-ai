# Collision Detector class
class CollisionDetector:

    def __init__(self, board):
        self.board = board

    # detects the first up collision given the position of a tile and determines how to respond to that collision
    def detect_up_collision(self, row, column):
        new_row = 0
        for i in range(1, self.board.rows):
            if row - i >= 0:
                if self.board.is_tile_occupied(row - i, column):
                    if self.board.board[row - i][column] == self.board.board[row][column]:
                        new_row = row - i
                    else:
                        new_row = row - i + 1
                    break
            else:
                break

        return new_row

    # detects the first down collision given the position of a tile and determines how to respond to that collision
    def detect_down_collision(self, row, column):
        new_row = 3
        for i in range(1, self.board.rows):
            if row + i <= self.board.rows - 1:
                if self.board.is_tile_occupied(row + i, column):
                    if self.board.board[row + i][column] == self.board.board[row][column]:
                        new_row = row + i
                    else:
                        new_row = row + i - 1
                    break
            else:
                break

        return new_row

    # detects the first left collision given the position of a tile and determines how to respond to that collision
    def detect_left_collision(self, row, column):
        new_column = 0
        for i in range(1, self.board.columns):
            if column - i >= 0:
                if self.board.is_tile_occupied(row, column - i):
                    if self.board.board[row][column - i] == self.board.board[row][column]:
                        new_column = column - i
                    else:
                        new_column = column - i + 1
                    break
            else:
                break

        return new_column

    # detects the first right collision given the position of a tile and determines how to respond to that collision
    def detect_right_collision(self, row, column):
        new_column = 3
        for i in range(1, self.board.columns):
            if column + i <= self.board.columns - 1:
                if self.board.is_tile_occupied(row, column + i):
                    if self.board.board[row][column + i] == self.board.board[row][column]:
                        new_column = column + i
                    else:
                        new_column = column + i - 1
                    break
            else:
                break

        return new_column
