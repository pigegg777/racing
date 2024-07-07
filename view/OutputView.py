import sys


def show_name_rule():
    print("차 이름을 입력하세요")


def show_name_error():
    print("이름은 1자 이상 5자 이햐이어야합니다")
    sys.exit("name")


def show_time_rule():
    print("시간을 입력하세요")


def show_time_errr():
    print("시간은 int 형태이어야 합니다")
    sys.exit("time")


def show_score(score_board: dict[str, int]):
    for name in score_board:
        print(name, end="")
        for score in range(score_board[name]):
            print("-", end="")
        print()


def show_winner(winner: list[str]):
    print("최종우승자는", end="")
    print(*winner, sep=",")
    print()
