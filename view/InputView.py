def read_car_names() -> list[str]:
    car_names = list(map(str, input().split(",")))

    def check_name_error(car_names_list: list[str]):
        for name in car_names_list:
            name = name.strip(" ")
            if len(name) > 5 or len(name) < 0:
                raise NameError

    check_name_error(car_names)
    return car_names


def read_time():
    try:
        time = int(input())
        return time
    except ValueError:
        raise ValueError
