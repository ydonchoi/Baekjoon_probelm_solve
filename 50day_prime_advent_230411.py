# 50일차: 소수 출현 비율(마지막 미션)_최영돈(문겸)

print("소수 출현 비율 v.0.1")
def isPrime(n):
    sieve = [False, False]+[True]*(n-1)
    primes = []
    for i in range(2, n+1):
        if sieve[i]:
            primes.append(i)
            for j in range(i*2, n+1, i):
                sieve[j]=False
    return primes
import time as t
while True:
    N = int(input('숫자 0을 입력하면 종료됩니다.\n숫자 입력(100의 배수): '))
    if N == 0:
        print(f'탈출! yeap!')
        break
    else:
        start=t.time()
        sum=0
        for k in range(int(N/10),N,int(N/10)):
            primes = isPrime(k)  # 소수 출현 갯수 구간별 집계로 이루어질 수 있도록 함수 수정 필요
            sum+=len(primes)
            print('{}~{}: {}개, {:.2f}%'.format((k-int(N/10)),k,len(primes),(len(primes)/N)*100))
        end=t.time()
        dtime=end-start
        print(f'{sum}개, 걸린시간: {dtime:.3f}초')