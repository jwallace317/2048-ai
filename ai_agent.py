from copy import deepcopy


class AIAgent:

    def __init__(self, board):
        self.board = board

    # def find_next_best_move(self):
    #     score_averages = []
    #     for direction in ['up', 'down', 'left', 'right']:
    #         score_sum = 0
    #         for i in range(5):
    #             board_copy = deepcopy(self.board)
    #             board_copy.move(direction)
    #             while not end_game(board_copy):
    #                 direction = generate_move(board_copy)
    #
    #                 if valid_move(board_copy, direction):
    #                     board_copy.move(direction)
    #                     board_copy.insert_random_tile()
    #
    #             score_sum += board_copy.score
    #
    #         score_average = score_sum / 5
    #         score_averages.append(score_average)
    #
    #     print('up: ' + str(score_averages[0]))
    #     print('down: ' + str(score_averages[1]))
    #     print('left: ' + str(score_averages[2]))
    #     print('right: ' + str(score_averages[3]))
    #
    #     max_score = max(score_averages)
    #     if max_score == score_averages[0]:
    #         return 'up'
    #     elif max_score == score_averages[1]:
    #         return 'down'
    #     elif max_score == score_averages[2]:
    #         return 'left'
    #     elif max_score == score_averages[3]:
    #         return 'right'


