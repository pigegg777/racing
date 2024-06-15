import random
import sys

def enter():
    try:
        print("경주할 자동차 이름을 입력하세요.(이름은 쉼표(,) 기준으로 구분)")
        car_names=list(map(str,input().split(',')))
        print(*car_names)
        print("반복횟수 입력")
        time=int(input())
        return time,car_names
    except:
        sys.exit(0)

def check_names(time,car_names):
    for name in range(len(car_names)):
        car_names[name]=car_names[name].strip(" ")
        if len(car_names[name])>5 or len(car_names[name])<0:
            print("오류입니다")
            sys.exit()    
                
def start() :
    time,car_names=enter()
    List_score=[]
    check_names(time,car_names)
    for _ in range(len(car_names)):
        List_score.append(0)          
    for _ in range(time):
        for num in range(len(car_names)):
            print(car_names[num],"",":",end="")
            score=random.randrange(0,10)
            if score>=4:
                List_score[num]+=1
            for _ in range(List_score[num]):
                print("-",end="")
            print()
        print()
    return List_score,car_names


def finish():
    List_score,car_names=start()
    winner=[]
    print("최종우승자 : ",end="")
    for rank in range(len(List_score)):
        if List_score[rank]==max(List_score):
            winner.append(car_names[rank])
    print(*winner,sep=", ")

finish()


