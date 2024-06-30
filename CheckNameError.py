class CheckNameError:
    def check_names(self, car_names):
        try:
            for name in car_names:
                name = name.strip(" ")
                if len(name) > 5 or len(name) < 0:
                    raise NameError
        except NameError as n:
            print("이름 오류입니다: {n}")
