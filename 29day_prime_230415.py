# 29일차: 함수를 활용하여 소수 판정하기_최영돈(문겸)
import time as t
print('소수판정 v.0.2')
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
    num = input('숫자입력:')
    if num == '':
        print('탈출! yeap!')
        break
    else:
        stime = t.time()
        n=int(int(num)**0.5)
        primes=isPrime(n)
        judge=[]
        for i in range(len(primes)):
            if int(num)%primes[i]==0: judge.append(i)
        if len(judge) == 0: print(f'정수 {num} : 소수입니다.')
        else: print(f'정수 {num} : 소수가 아닙니다.')
        etime = t.time()
        print('걸린 시간: %.2f 초'%(etime-stime))
