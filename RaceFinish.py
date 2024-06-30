from MainRace import MainRace


class RaceFinish:
    def finish_race(self,score_board):
        winner = []
        for name in score_board:
            if score_board[name] == max(score_board.values()):
                winner.append(name)
        print("최종우승자는")
        print(*winner, sep=", ")
