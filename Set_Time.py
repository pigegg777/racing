import sys
class Set_Time:
    def set_time(self):
        try:
            print("시간을 입력하세요")
            time = int(input())
            return time
        except:
            sys.exit()