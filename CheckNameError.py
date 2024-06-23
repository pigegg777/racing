from SetCarNames import SetCarNames


class CheckNameError:
    set_car_names = SetCarNames()

    def check_names(self):
        try:
            car_names = self.set_car_names.car_names()
            for name in car_names:
                name = name.strip(" ")
                if len(name) > 5 or len(name) < 0:
                    raise NameError
        except NameError as n:
            print("이름 오류입니다: {n}")
