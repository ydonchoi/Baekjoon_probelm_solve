# 문제번호: 2581
# 소수의 합과 최소값 구하기
# url: https://www.acmicpc.net/problem/2581
# 출처: 나의 네이버 블로그 (blog.naver.com/ydonchoi83)
# 2022.06.19.~2022.07.01.
# Revised on 2024. 06. 23.

#########################
# [문제]
# 자연수 M과 N이 주어질 때 M이상 N이하의 자연수 중 소수인 것을 모두 골라,
# 이들 소수의 합과 최소값을 찾는 프로그램을 작성하시오.
#########################

''' I knew old expression using Eratosthenes's sieve.
    And this time, I have learnt two ways more efficient.
    So.. update adopting these ways '''

def is_prime1(num):
    ''' the first way to check prime numbers, i.e. Eratosthenes's sieve '''
    for x in range(2, num):
        if num % x == 0:
            return False
    return True

def is_prime2(num):
    ''' the second way to check prime numbers, i.e. Eratosthenes's sieve '''
    if num == 1 or num <= 0:
        return False
    for x in range(2, floor(sqrt(num))+1):
        if num % x == 0:
            return False
    return True

def main():
    print('you input two integers "m" and "n"(m<n) with one space between them)')
    m, n = map(int, input('input two integers: ').split())
    nums = range(m, n+1)
    primes = [x for x in nums if is_prime1(x)]
    primes2 = [x for x in nums if is_prime2(x)]

    print(f'sum : {sum(primes)} | min : {min(primes)} | len : {len(primes)}')
    print(f'sum : {sum(primes2)} | min : {min(primes2)} | len : {len(primes2)}\n')
    print(primes'\n')
    print(primes2)

if __name__ == "__main__":
    from math import floor, sqrt
    main()

# fin.