from Set_Car_Names import Set_Car_Names

class Check_Name_Error:
    def check_names(self):
        try:
            car_names= Set_Car_Names.car_names()
            for name in car_names:
                name=name.strip(" ")
                if len(name)>5 or len(name)<0:
                    raise NameError
                else:
                    return Set_Car_Names.car_names
        except NameError as n:
            print("이름 오류입니다: {n}")

