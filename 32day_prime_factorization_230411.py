# 32일차: 소인수 분해(v.0.1)_최영돈(문겸)

print("소인수 분해 v.0.1")
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
    N = input('정수: ')
    if N == '': break
    else:  
        n = int(N)
        primes = isPrime(n)
        print("소인수 분해: ",end='')
        i=0
        while i in range(len(primes)):
            if str(n in primes) == 'True':
                print(n)
                break
            elif n%primes[i] == 0:
                print(f'{primes[i]}',end=' X ')
                n = n//primes[i]
            else: i+=1