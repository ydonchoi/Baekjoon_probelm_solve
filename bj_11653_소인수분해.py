# #파이썬 #백준 
# #11653번문제 #소인수분해문제
# - 출처: 나의 네이버 블로그 (blog.naver.com/ydonchoi83)
# - 기간: 2022.06.19.~2022.07.01.

# [문제]
# 정수 N이 주어졌을 때, 소인수분해하는 프로그램을 작성하시오.
# - 첫째 줄에 정수 N (1 ≤ N ≤ 10,000,000)이 주어진다.

import random
def prime_factor(n):
	quotient = random.randint(2,n)
	sieve = [False, False] + [True]*(n-1)
	primes = []
	for i in range(2, n+1):
		if sieve[i]:
			primes.append(i)
			for j in range(i*2, n+1, i):
				sieve[j] = False
	print('정수: ', quotient, '\n[소인수분해 결과]')
	k = 0
	result = []
	while True:
		if quotient >= primes[k]:
			if quotient % primes[k] == 0:
				print(primes[k], '|', quotient//primes[k])
				result.append(primes[k])
				quotient = quotient//primes[k]
			else:
				k += 1
		else:
			break

prime_factor(1000000)

# fin.