#파이썬 #백준 #문제풀이 #10826번 #피보나치수4 #최영돈(231021,band.us/@ydonchoi)
'''
(문제)
피보나치 수는 0과 1로 시작한다.
3번째 수부터는 앞의 두 수의 합으로 구성된다.
n번째 피보나치 수를 출력하시오.
ex) n=17일떄 피보나치 수열은 다음과 같다.
[0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987]
'''
N = int(input('몇 번째 피보나치 수를 출력하시겠습니까?:'))
피보나치 = [0,1]
if N <= 2:
    print(피보나치[N-1])
else:
    for n in range(2, N):
            temp = 피보나치[n-2] + 피보나치[n-1]
            피보나치.append(temp)
    print(피보나치[n])  # fin.
    
'''
(모범답안1)
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

(모범답안2)
def fibonacci(n):
    dp = [0] * (n+1)
    dp[0], dp[1] = 0, 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

T = int(input())
for _ in range(T):
    N = int(input())
    print(fibonacci(n))
'''