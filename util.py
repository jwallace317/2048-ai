def different_boards(antecedent_board, consequent_board):
    for row in range(4):
        for column in range(4):
            if antecedent_board[row][column] != consequent_board[row][column]:
                return True

    return False
