#백준 #문제풀이 #14916번 #거스름돈 #최영돈(231021,band.us/@ydonchoi)
'''
(Q)
A는 편의점 카운터에서 일한다.
손님들은 거스름돈으로 2원짜리 동전과 5원짜리 동전으로만 받길 원한다.
동전의 갯수를 최소로 하여 거스름돈을 드리는 프로그램을 작성하시오.
(예)
거스름돈이 15원일 경우, 5원짜리 동전 3개
거스름돈이 13원일 경우, 5원짜리 동전 1개와 2원짜리 동전 4개이므로 총 5개
'''

R = int(input('거스름돈은 얼마인가요?:'))
M = R
for i in range(1,(R//5)+1):
    if (R%i)%2 == 0:
        for x in range(i+1):
            m = ((-3*x)+R)//2
            if M >= m: M = m
    else: pass
print(f'거스름돈: {R}원\n5원짜리 동전: {x}개\n2원짜리 동전: {M-x}개\n최소동전갯수: {M}개')  # fin.


'''
(모범답안1)
def solution(money, price):
    change = money - price
    coins = 0
    while change > 0:
        if change >= 500:
            change -= 500
            coins += 1
        elif change >= 100:
            change -= 100
            coins += 1
        elif change >= 50:
            change -= 50
            coins += 1
        elif change >= 10:
            change -= 10
            coins += 1
        elif chage >= 5:
            change -= 5
            coins += 1
        else:
            chage -= 1
            conis += 1
    retunr coins

(모범답안2)
def solution(money, price):
    change = money - price
    coins = 0
    coins += change // 500
    change %= 500
    coins += change // 100
    change %= 100
    coins += change // 50
    change %= 50
    coins += change // 10
    change %= 10
    coins += change // 5
    change %= 5
    coins += change // 1
    return coins

money, price = map(int, input().split())
print(solution(money, price))
'''