# 34일차: 소인수 분해(v.0.2)_최영돈(문겸)

print("소인수 분해 v.0.2")
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
    N = input('정수(숫자 없이 엔터 입력시 종료): ')
    if N == '':
        print('탈출! YEAP!')
        break
    else:        
        n = int(N)  
        primes = isPrime(n)
        print("소인수 분해: ",end='')
        i=0
        tmp=[]
        while i in range(len(primes)):
            if n%primes[i] == 0:
                tmp.append(primes[i])
                n = n//primes[i]
            elif str(n in primes) == 'True':
                tmp.append(n)
                break
            else: i+=1
        for i in set(tmp):
            cnt=0
            for j in range(len(tmp)):
                if i == tmp[j]: cnt+=1
            print(f'{i}^{cnt}',end=' x ')
        print()