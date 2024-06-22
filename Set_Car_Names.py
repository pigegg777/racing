import sys
from Check_Name_Error import Check_Name_Error
class Set_Car_Names:
    car_names = []
    def set_car_names(self):
        try:
            car_names1 = list(map(str, input("경주할 자동차 이름을 입력하세요.(이름은 쉼표(,) 기준으로 구분)").split(',')))
            Set_Car_Names.car_names = car_names1
            Check_Name_Error.check_names()
            return Set_Car_Names.car_names
        except:
            sys.exit(0)
    def set_score_board(self):
        try:
            score_board = {}
            for name in Set_Car_Names.car_names:
                score_board[name] = 0
            return score_board
        except:
            sys.exit(0)

