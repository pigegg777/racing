from Main_Race import Main_Race

class Race_Finish:
    def finish_race(self):
        score_board=Main_Race.race_start()
        winner=[]
        for name in score_board:
            if score_board[name]==max(score_board.values()):
                winner.append(name)
        print(*winner,sep=", ")