# 30일차: 범위 내 소수 갯수 구하기_최영돈(문겸)
print('소수판정 v.0.3(범위 내 소수 개수)')
import time as t
def isPrime(n):
    sieve = [False, False]+[True]*(n-1)
    primes = []
    for i in range(2, n+1):
        if sieve[i]:
            primes.append(i)
            for j in range(i*2, n+1, i):
                sieve[j]=False
    return primes
while True:
    num1 = input('범위 시작:')
    if num1 == '':
        print('탈출! yeap!')
        break
    else:
        num1=int(num1)
        num2 = int(input('범위 끝:'))
        stime=t.time()
        primes1 = isPrime(num1)
        primes2 = isPrime(num2)
        for i in range(len(primes1)):
            primes2.remove(primes1[i])
        etime=t.time()
        print('소수 갯수 = {}개, 걸린 시간: {:.2f}초'.format(len(primes2), etime-stime))