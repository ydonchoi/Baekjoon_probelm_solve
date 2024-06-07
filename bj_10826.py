# 문제번호: 10826
# 피보나치수4
# url: https://www.acmicpc.net/problem/10826
# 23.10.21.

###########################
## (문제)
## 피보나치 수는 0과 1로 시작한다.
## 3번째 수부터는 앞의 두 수의 합으로 구성된다.
## n번째 피보나치 수를 출력하시오.
## ex) n=17일떄 피보나치 수열은 다음과 같다.
## [0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987]
###########################

# My_solution_revised(24.06.07.)
def fibo_4(num: int) -> list:
    if num == 1:
         return 0
    if num < 4:
         return 1
    else:
         return fibo_4(num-2) + fibo_4(num-1)

def main():
    N = int(input('몇 번째 피보나치 수를 출력하시겠습니까?:'))
    res = [fibo_4(idx) for idx in range(1,N+1)]
    print(len(res))
    print(res)

if __name__== "__main__":
     main()

# fin.



# '''
# (모범답안1)
# def fibonacci(n):
#     if n == 0 or n == 1:
#         return n
#     return fibonacci(n-1) + fibonacci(n-2)

# (모범답안2)
# def fibonacci(n):
#     dp = [0] * (n+1)
#     dp[0], dp[1] = 0, 1
#     for i in range(2, n+1):
#         dp[i] = dp[i-1] + dp[i-2]
#     return dp[n]

# T = int(input())
# for _ in range(T):
#     N = int(input())
#     print(fibonacci(n))
# '''