import sys

class Race_Setting:
    def set_CarNames():
        try:
            print("경주할 자동차 이름을 입력하세요.(이름은 쉼표(,) 기준으로 구분)")
            car_names=list(map(str,input().split(',')))
            return car_names
        except:
            sys.exit(0)
    def set_time():
        try:
            print("시간을 입력하세요")
            time=int(input())
            return time
        except:
            sys.exit()
    def score_board(CarNames):
        CarNames=Race_Setting.set_CarNames()
        score_board={}
        for name in CarNames:
            score_board[name]=0
        return score_board
            