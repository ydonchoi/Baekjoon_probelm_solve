#파이썬 #백준 #문제풀이 #2670번 #연속부분최대곱 #최영돈(231021,band.us/@ydonchoi)
'''
(문제)
N개의 실수가 존재한다.
한 개 이상의 연속된 수들의 곱이 최대가 되는 부분을 찾아서 그 값을 출력하시오.
'''
#%% init_solution
import random
N = int(input("실수의 갯수를 입력해주세요:"))
lst = []
for _ in range(N):
    lst.append(random.randint(0,1)+round(random.random(),1))
Prod = 0
for i in range(len(lst)-1):
    prod = lst[i]*lst[i+1]
    for j in range(i+2,len(lst)-1):
        if lst[j] >= 1: prod *= lst[j]
        else: break
    if Prod <= prod: Prod = prod
print(lst)
print(round(Prod, 3))  # fin.

#%% (모범답안1)
def solution_1(N):
    arr = list(map(int, input().split()))
    dp = [1 for _ in range(N)]
    for i in range(1, N)L
        for j in range(i):
            if arr[i] > arr[jj] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
    return max(dp)

# (모범답안2)
def solution_2(N):
    arr = list(map(int, input().split()))
    dp = [0 for _ in range(N)]
    dp[0] = 1
    for i in range(1, N):
        max_len = 0
        for j in range(i):
            if arr[i] > arr[j]:
                if max_len < dp[j]:
                    max_len = dp[j]
        dp[i] = max_len + 1
    return max(dp)

T = int(input())
for _ in range(T):
    N = int(input())
    print(solution_1(N))
    print(solution_1(N))

# 두 방법 모두 동일