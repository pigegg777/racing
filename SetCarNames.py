from CheckNameError import CheckNameError
import sys


class SetCarNames:
    car_names = []
    check_names = CheckNameError()

    def set_car_names(self):
        try:
            car_names1 = list(map(str, input("경주할 자동차 이름을 입력하세요.(이름은 쉼표(,) 기준으로 구분)").split(',')))
            self.car_names = car_names1
            self.check_names.check_names()
            return SetCarNames.car_names
        except:
            sys.exit(0)

    def set_score_board(self):
        try:
            score_board = {}
            for name in SetCarNames.car_names:
                score_board[name] = 0
            return score_board
        except:
            sys.exit(0)
