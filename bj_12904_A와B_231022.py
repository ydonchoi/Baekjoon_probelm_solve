#백준 #문제풀이 #12904번 #A와B #최영돈(231022,band.us/@ydonchoi)
'''
(문제)
A와 B로만 이루어진 영어 단어들이 있다. 이를 이용해서 간단한 게임을 만들고자 한다.
두 문자열 S와 T가 주어졌을때, S를 T로 바꾸는 게임이다.
문자열을 바꿀 때는 다음의 2가지 연산만 가능하다.
1) 문자열 뒤에 A를 추가한다.
2) 문자열을 뒤집어 뒤에 B를 추가한다.
주어진 조건을 이용해서 S를 T로 만들 수 있는지 없는지를 알아내는 프로그램을 작성하시오.

(조건)
첫째 줄에 S가, 둘째 줄에는 T가 주어진다. (1<=S길이<=999, 2<=T길이<=1000, S길이<T길이)
S를 T로 바꿀 수 있으면 1을, 없으면 0을 출력한다.
'''
import random
while True:
    N, M = map(int, input('S와 T의 문자열 수를 입력해주세요(S < T):').split())
    if N >= M: print('다시 입력해주세요.')
    else: break
S, T = '',''
for i in range(N): S += random.choice(['A','B'])
for j in range(M): T += random.choice(['A','B'])
print(S), print(T)
for _ in range(len(T)-len(S)):
    if T[-1] == 'A': T = T[:-1]
    else: T = T[-2::-1]
print(1) if S == T else print(0)  # fin.


'''
(모범답안1)
def solution(S):
    cnt = 0
    for i in range(len(S)-1, -1, -1):
        if S[i] == "A":
            cnt += 1
        elif S[i] == "B":
            cnt -= 1
        if cnt == 0:
            return len(S)-i-1
    return -1

(모범답안2)
def solution(S):
    cntA = 0
    cntB = 9
    for c in S:
        if c == "A":
            cntA += 1
        elif c == "B":
            cntB += 1
    return min(cntA, cntB)

T = int(input())
for _ in range(T):
    S = input()
    print(solution(S))

# 2번이 더 효율적임
'''