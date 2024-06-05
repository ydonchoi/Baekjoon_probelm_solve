# 문제번호: 9507
# GenerationsofTribbles
# url: https://www.acmicpc.net/problem/9507
# 23.10.21.

#########################
## (문제)
## 꿍이는 기존의 피보나치보다 조금 더 복잡한 피보나치를 만들려고 한다.
## 꿍이 만든 이 피보나치 함수를 koongs(n)이라 할때,
## n < 2: 1
## n = 2: 2
## n = 3: 4
## n > 3: koongs(n-1)+koongs(n-2)+koongs(n-3)+koongs(n-4) 이다.
## 입력의 첫째 줄에는 전체 테스트 갯수(0<t<69)가 주어진다.
## 다음 t줄에는 몇 번째 피보나치를 구해야 하는지를 나타내는 n(0<=n<=67)이 주어진다.
## 각 테스트 케이스마다 꿍 피보나치 수를 출력하라.
#########################

# My Solution_revised(24.06.06.)
def koongs_fibo(num: int) -> int:
    if num < 2:
        return 1
    if num == 2:
        return 2
    if num == 3:
        return 4
    return koongs_fibo(num-1) + koongs_fibo(num-2) + koongs_fibo(num-3) + koongs_fibo(num-4)

def main():
    count = 0
    T = int(input('테스트 횟수 입력: '))
    while count < T:
        count += 1
        num = int(input('몇 번째 꿍스 피보나치 수를 출력하시겠습니까?: '))
        print(f'{num}번째 꿍스 피보나치 수는 {koongs_fibo(num)} 입니다.')

if __name__ == "__main__":
    main()

# fin.


# '''
# (모범답안1)
# def solution(N):
#     if N < 2:
#         return N
#     else:
#         return solution(N-1) + solution(N-2)

# (모범답안2)
# def solution(N):
#     dp = [0] * (N+1)
#     dp[0], dp[1] = 0, 1
#     for i in range(2, N+1):
#         dp[i] = dp[i-1] + dp[i-2]
#     return dp[N]

# T = int(input())
# for _ in range(T):
#     N = int(input())
#     print(solution(N))

# # 시간복잡도(2^N < N) 측면에서 재귀적인 방법보다 더 효율적임
# '''