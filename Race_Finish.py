import MainRace

class Race_Finish:
    def finish_race(self):
        score_board=MainRace.race_start()
        winner=[]
        for name in score_board:
            if score_board[name]==max(score_board.values()):
                winner.append(name)
        print(*winner,sep=", ")