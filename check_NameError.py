from RaceSet import Race_Setting

class check_names:
    def check_names(CarNames):
        CarNames=Race_Setting.set_CarNames()
        for name in range(len(CarNames)):
            CarNames[name]=CarNames[name].strip(" ")
            if len(CarNames[name])>5 or len(CarNames[name])<0:
                raise NameError
    def call_NameError():
        try:
            check_names()
        except NameError as n:
            print("이름 오류입니다: {n}")