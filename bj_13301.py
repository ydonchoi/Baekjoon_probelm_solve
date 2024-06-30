# 문제번호: 13301
# 타일장식물
# url: https://www.acmicpc.net/problem/13301
# 23.10.21.

#########################
# (문제)
# 타일 장식물은 정사각형의 타일이다.
# 한변의 길이가 1인 정사각형 타일로 시작하여 앵무조개의 나선 모양처럼 점점 큰 타일을 붙인 형태로 이루어져있다.
# 타일의 한 변의 길이 순서는 [1,1,2,3,5,8,13...]순으로 이루어진다.
# n개의 타일로 구성된 직사각형의 둘레를 구하는 프로그램을 작성하시오.
#########################

'''(해결방안)
피보나치 이용 (n>=2인 경우)'''


def fibo(num: int) -> int:
    return 1 if num < 2 else fibo(num-2) + fibo(num-1)


def fibo_deco(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return wrapper


@fibo_deco
def length_list(num: int) -> list:
    return [fibo(n) for n in range(num)]


def length_of_surrounding_rectangle(length: list, num: int) -> int:
    if num < 2:
        return (4*length[num-1])
    else:
        return ((2*length[num-2])+(4*length[num-1]))


def main():
    N = int(input('몇 개의 타일로 구성하시겠습니까?:'))
    length = length_list(N)
    print(length)
    surroundings = length_of_surrounding_rectangle(length, N)
    print(f'직사각형 둘레의 길이={surroundings}')


if __name__ == "__main__":
    main()

# fin.

# (모범답안1)
# def solution(N):
#     dp = [0] * (N+1)
#     dp[1], dp[2] = 1, 1
#     for i in range(3, N+1):
#         dp[i] = dp[i-1] + dp[i-2]
#     return 2 * (dp[N-1]+dp[N])

# (모범답안2)
# def solution(N):
#     return 2 * (F(N+1)-F(N))
# def F(N):
#     if N <= 2:
#         return N
#     return F(N-1) + F(N-2)

# T = int(input())
# for _ in range(T):
#     N = int(input())
#     print(solution(N))
# # 두 번째가 더 효율적임
