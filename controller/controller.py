from model import MainRace
from model import SetScoreBoard
from view import InputView, OutputView

race = MainRace.MainRace()


def set_race():
    try:
        OutputView.show_name_rule()
        car_names = InputView.read_car_names()
        OutputView.show_time_rule()
        time = InputView.read_time()
        score_board = SetScoreBoard.set_score_board(car_names)

        return score_board, time
    except NameError:
        OutputView.show_name_error()
    except ValueError:
        OutputView.show_time_errr()


def race_start() -> dict[str, int]:
    score_board, time = set_race()
    race.start(score_board)
    for _ in range(time):
        score_board = race.start(score_board)
        OutputView.show_score(score_board)
    return score_board


def race_finish():
    final_score_board = race_start()
    winner = race.finish(final_score_board)
    OutputView.show_winner(winner)
