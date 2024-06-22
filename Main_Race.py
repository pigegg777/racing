from Set_Time import Set_Time
from Set_Car_Names import Set_Car_Names
import random


class Main_Race:
    def race_start(self) :
        car_names=Set_Car_Names.set_car_names()
        score_board=Set_Car_Names.set_score_board()
        time=Set_Time.set_time()
        for _ in range(time):
            for name in car_names:
                print(name,"",":",end="")
                score=random.randrange(0,10)
                if score>=4:
                    car_names[name]+=1
                for _ in range(car_names[name]):
                    print("-",end="")
                print()
            print()
        return score_board