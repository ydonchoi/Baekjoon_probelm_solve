#코딩 #파이썬 #파이썬기초코딩밴드미션
#50일차: 소수 출현 비율(마지막 미션)_최영돈(문겸)
#예) 백만일 경우 1초 이내, 천만일 경우 5초 이내로 완성한다.  ---> 현재로는 무리.. 실패..!!(40초 가량 걸리다니..ㅜ.ㅜ)
print("소수 출현 비율 v.0.1")
def isPrimes(m):
    primes=[]
    sieve = [False, False]+[True]*(m-1)
    for i in range(2,m+1):
        if sieve[i]:
            primes.append(i)
            for j in range(i*2, m+1, i):
                sieve[j]=False
    return primes
import time as t
while True:
    N = int(input('숫자 0을 입력하면 종료됩니다.\n숫자 입력(100의 배수): '))
    if N == 0 :
        print(f'탈출! yeap!')
        break
    elif N < 100:
        print('잘못 입력하였습니다. 100의 배수를 입력하세요.')
    else:
        start=t.time()
        sum=0
        primes_blw=isPrimes(int(N/10))
        sum+=len(primes_blw)
        print(f'0~{int(N/10)}: {len(primes_blw)}개, {(len(primes_blw)/N*100):.2f}%')
        for n in range(int(N/10),N,int(N/10)):
            primes_all,primes_exp=[],[]
            sieve = [False, False]+[True]*(n+int(N/10)-1)
            for i in range(1,n+int(N/10)+1):
                if sieve[i]:
                    primes_all.append(i)
                    for j in range(i*2, n+int(N/10)+1, i):
                        sieve[j]=False
            for k in range(1,n+1):
                if sieve[k]:
                    primes_exp.append(k)
                    for l in range(k*2,n+1,k):
                        sieve[l]=False
            primes=[a for a in primes_all if not a in primes_exp or primes_exp.remove(a)]
            sum+=len(primes)
            print('{}~{}: {}개, {:.2f}%'.format(n,(n+int(N/10)),len(primes),(len(primes)/N)*100))
        end=t.time()
        dtime=end-start
        print(f'{sum}개, 걸린시간: {dtime:.3f}초')