import sys


class SetScoreboard:
    def set_scoreboard(self, car_names: list):
        try:
            score_board = {}
            for name in car_names:
                score_board[name] = 0
            return score_board
        except:
            sys.exit(0)
