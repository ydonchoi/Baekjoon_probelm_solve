# 문제번호: 2670
# 연속 부분 최대 곱
# url: https://www.acmicpc.net/problem/2670
# 23.10.21

#########################
# (문제)
# N개의 실수가 존재한다.
# 한 개 이상의 연속된 수들의 곱이 최대가 되는 부분을 찾아서 그 값을 출력하시오.
#########################


def generate_random_float(num: int) -> list[float]:
    return [random.randint(0, 1)+round(random.random(), 1) for _ in range(num)]


def my_solution(nums: list[int]) -> int:
    Prod = 0
    for i in range(len(nums)-1):
        prod = nums[i]*nums[i+1]
        for j in range(i+2, len(nums)-1):
            if nums[j] >= 1:
                prod *= nums[j]
            else:
                break
        if Prod <= prod:
            Prod = prod
    return Prod


def main():
    N = int(input("실수의 갯수를 입력해주세요:"))
    nums = generate_random_float(N)
    prod = my_solution(nums)
    print(nums)
    print(round(prod, 3))


if __name__ == '__main__':
    import random
    main()

# fin.

# %% (모범답안1)
# def sample_solution_1(N):
#     arr = list(map(int, input().split()))
#     dp = [1 for _ in range(N)]
#     for i in range(1, N):
#         for j in range(i):
#             if arr[i] > arr[jj] and dp[i] < dp[j] + 1:
#                 dp[i] = dp[j] + 1
#     return max(dp)

# # (모범답안2)
# def sample_solution_2(N):
#     arr = list(map(int, input().split()))
#     dp = [0 for _ in range(N)]
#     dp[0] = 1
#     for i in range(1, N):
#         max_len = 0
#         for j in range(i):
#             if arr[i] > arr[j]:
#                 if max_len < dp[j]:
#                     max_len = dp[j]
#         dp[i] = max_len + 1
#     return max(dp)

# T = int(input())
# for _ in range(T):
#     N = int(input())
#     print(sample_solution_1(N))
#     print(sample_solution_1(N))

# 두 방법 모두 동일
