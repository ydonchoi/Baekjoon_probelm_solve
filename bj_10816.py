# 문제번호: 10816
# 숫자카드2
# url: https://www.acmicpc.net/problem/10816
# 23.10.29.

###########################
## (문제)
## 정수가 적힌 숫자카드 갯수가 첫번째 줄에 주어진다.
## 보유한 숫자카드의 숫자가 두번째 줄에 주어진다.
## 임의로 보유한 숫자카드 중에서 주어진 숫자를 가진 카드를 몇 장 보유했는지를 출력하시오.
###########################

# My_solution
def suffle_cards(num: int) -> list:
    return [random.randint(1,14) for _ in range(num)]

def counting_cards(number: int, cards: list) -> int:
    return cards.count(number)

def main():
    num = int(input('the number of having cards: '))
    number = int(input('the number of counting card (under 14): '))
    cards = suffle_cards(num)
    counting = counting_cards(number, cards)
    print(counting)

if __name__ == "__main__":
    import random
    main()

# fin.



# '''
# (모범답안1)
# def solution(N):
#     sum = 0
#     cards = list(range(1, N+1))
#     while len(cards) > 1:
#         sum += cards.pop(0)
#     return sum

# (모범답안2)
# def solution(N):
#     return sum(range(1, N+1))//2

# T = int(input())
# for _ in range(T):
#     N = int(input())
#     print(solution(N))

# # 두 번째가 첫 번째보다 더 효율적임
# '''