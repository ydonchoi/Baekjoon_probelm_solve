# 28일차: 함수를 활용하여 소수 판정하기_최영돈(문겸)
print('소수판정 v.0.1')
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
        num=int(num)
        if isPrime(num)[-1]==num:
            print(f'{num}는 소수입니다.')
        else: print(f'{num}는 소수가 아닙니다.')