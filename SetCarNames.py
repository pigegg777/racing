from CheckNameError import CheckNameError
import sys


class SetCarNames:
    car_names = []
    check_names = CheckNameError()
    def set_car_names(self):
        try:
            car_names = list(map(str, input("경주할 자동차 이름을 입력하세요.(이름은 쉼표(,) 기준으로 구분)").split(',')))
            self.check_names.check_names(car_names)
            return car_names
        except:
            sys.exit(0)
