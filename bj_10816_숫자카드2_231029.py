#백준 #문제풀이 #10816번 #숫자카드2 #최영돈(231029,band.us/@ydonchoi)
'''
(문제)
정수가 적힌 숫자카드 갯수가 첫번째 줄에 주어진다.
보유한 숫자카드의 숫자가 두번째 줄에 주어진다.
임의로 보유한 숫자카드 중에서 주어진 숫자를 가진 카드를 몇 장 보유했는지를 출력하시오.
'''
import random
N = int(input('보유카드 매수 입력(14장 이하:'))
card = random.sample(range(1, 15), N)
num = int(input('카운팅할 숫자 입력(14 이하):'))
cnt = 0
for i in range(len(card)):
    if card[i] == num: cnt +=1
print(N), print(num), print(cnt)  # fin.


'''
(모범답안1)
def solution(N):
    sum = 0
    cards = list(range(1, N+1))
    while len(cards) > 1:
        sum += cards.pop(0)
    return sum

(모범답안2)
def solution(N):
    return sum(range(1, N+1))//2

T = int(input())
for _ in range(T):
    N = int(input())
    print(solution(N))

# 두 번째가 첫 번째보다 더 효율적임
'''