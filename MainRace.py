from SetTime import Set_Time
from SetCarNames import SetCarNames
import random


class MainRace:
    set_car_name = SetCarNames()
    set_time = Set_Time()

    def race_start(self):
        car_names = self.set_car_name.set_car_names()
        score_board = self.set_car_name.set_score_board()
        time = self.set_time.set_time()
        for _ in range(time):
            for name in car_names:
                print(name, "", ":", end="")
                score = random.randrange(0, 10)
                if score >= 4:
                    car_names[name] += 1
                for _ in range(car_names[name]):
                    print("-", end="")
                print()
            print()
        return score_board
