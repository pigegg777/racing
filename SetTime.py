import sys


class SetTime:
    def set_time(self):
        try:
            print("횟수를 입력하세요")
            time = int(input())
            return time
        except:
            sys.exit()
