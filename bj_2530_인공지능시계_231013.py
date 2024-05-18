#파이썬 #백준 #문제풀이 #2530번 #인공지능시계문제 #최영돈(231013,band.us/@ydonchoi)
'''
(문제)
훈제오리구이를 시작하는 시각과 오븐구이를 하는데 필요한 시간이 초 단위로 주어졌을 떄,
오븐구이가 끝나는 시각을 계산하는 프로그램을 작성하시오.
'''
#%% init_solution
import datetime
H = int(datetime.datetime.today().strftime("%H"))
M = int(datetime.datetime.today().strftime("%M"))
S = int(datetime.datetime.today().strftime("%S"))
print(f'현재시각:{H} {M} {S}')
duration = int(input("소요시간(초):"))
print(duration)
if duration >= 60:
    if duration >= 3600:
        h = int(duration / 3600)
        H += h
    else:
        h=0
    m = int((duration-(3600*h))/60)
    M += m
else:
    m = 0
S += int(duration-(3600*h+60*m))
if S >= 60: M += 1; S -= 60
if M >= 60: H += 1; M -= 60
if H >= 24: H -= 24
print(f'종료시각:{H} {M} {S}')    # fin.

#%% (모범답안1)  # 다른 solution들과 종료시각 출력값이 다르다??
def solution_1(A, B, C, D):
    hour = A+D // (60*60)
    minute = (D%(60*60))//60
    second = D%60
    return hour, minute, second

# (모범답안2)
def solution_2(A, B, C, D):
    hour = A+D // (60*60)
    minute = B+(D%(60*60))//60
    second = C+D%60
    if second >= 60:
        minute += 1
        second -= 60
    if minute >= 60:
        hour += 1
        minute -= 60
    return hour, minute, second

T = int(input())
for _ in range(T):
    A, B, C = map(int, input().split())
    D = int(input())
    print(*solution_1(A, B, C, D))
for _ in range(T):
    A, B, C = map(int, input().split())
    D = int(input())
    print(solution_2(A, B, C, D))

# 두 가지 방법 모두 동일