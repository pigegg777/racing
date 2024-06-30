from SetCarNames import SetCarNames
from SetScoreboard import SetScoreboard
from SetTime import SetTime
from MainRace import MainRace
from RaceFinish import RaceFinish

SC = SetCarNames()
ST = SetTime()
SB = SetScoreboard()
MR = MainRace()
RF = RaceFinish()

car_names = SC.set_car_names()
time = ST.set_time()
score_board = SB.set_scoreboard(car_names)
final_scoreboard = MR.start(score_board, time)
RF.finish_race(final_scoreboard)
