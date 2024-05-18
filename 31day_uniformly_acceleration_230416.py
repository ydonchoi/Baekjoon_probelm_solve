# 31일차: 엘리베이터 등가속도운동-1차시도 (최영돈(문겸))

# 엘리베이터 층간 이동시간을 감소시켜라.
# 처음 속도가 가장 늦고 맨 마지막 층간 이동이 가장 빠르다.
# 0층부터 x층까지 층간 이동할 때 걸리는 시간을 1초에서 0초까지 줄인다.

# 이동할 층 수 입력
# 속도는 등속도 = 1
# 수식 = (잔여층수 / 입력층수)*속도
# 출력

while True:
    floor = input('가고자 하는 층수:')
    if floor == '':
        print('탈출! yeap!')
        break
    else:
        movement_time=[]
        floor = int(floor)
        speed = 1
        for i in range(floor+1):
            movement_time.append(((floor-i)/floor)*speed)
            print('{}층 이동 시간: {:.2f} 초'.format(i,movement_time[i]))
        print(f'{floor}층 도착!')