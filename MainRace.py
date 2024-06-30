
import random


class MainRace:
    def start(self,score_board,time):
        for _ in range(time):
            for name in score_board:
                print(name, "", ":", end="")
                score = random.randrange(0, 10)
                if score >= 4:
                    score_board[name] += 1
                for _ in range(score_board[name]):
                    print("-", end="")
                print()
            print()
        return score_board
