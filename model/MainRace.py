import random


class MainRace:
    def start(self, score_board: dict[str, int]) -> dict[str, int]:
        for name in score_board:
            score = random.randrange(0, 10)
            if score >= 4:
                score_board[name] += 1

        return score_board

    def finish(self, score_board: dict[str, int]) -> list[str]:
        winner = []
        for name in score_board:
            if score_board[name] == max(score_board.values()):
                winner.append(name)
        return winner
