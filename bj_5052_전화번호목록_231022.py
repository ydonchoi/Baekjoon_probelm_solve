#백준 #문제풀이 #5052번 #전화번호목록 #최영돈(231021,band.us/@ydonchoi)
'''
(문제)
주어진 전화번호의 목록에 일관성이 있는지를 구하는 프로그램을 작성하시오.
일관성이 있으려면 하나의 번호가 다른 번호의 접두어인 경우가 없어야 한다.

(조건)
첫째 줄에는 테스트 케이스 수 t(1<=t<=50)가 주어진다.
각 테스트 케이스의 첫째 줄에는 전화번호의 수 n(1<=n<=10000)이 주어지고, 다음의 n개 줄에는 전화번호들이 주어진다.
전화번호의 길이는 길어야 10자리이며, 하나의 목록에서 동일한 전화번호는 없다.
'''
import random
T = int(input('테스트 횟수(50회 이하 입력):'))
print(T)
cnt = 0
tmp = []
while True:
    if T == cnt: break
    else:
        cnt += 1
        n = int(input('전화번호 갯수:'))
        print(n)
        tel = random.sample(range(1,10000000000), k=n)
        tel.sort()
        for i in range(n):
            print(tel[i])
            for j in range(i+1, n):
                if str(tel[i]) == str(tel[j])[:len(str(tel[i]))] : tmp.append(0)
                else: tmp.append(1)
    print('NO') if tmp.count(0) > 0 else print('YES')   # fin.


'''
(모범답안1)
def solution(S):
    N = len(S)
    for i in range(N):
        if S[i] != S[N-i-1]:
            return False
    return True

(모범답안2)
def solution(S):
    N = len(S)
    return S[:N//2] == S[N//2:][::-1]

T = int(input())
for _ in range(T):
    S = input()
    print(solution(S))
'''