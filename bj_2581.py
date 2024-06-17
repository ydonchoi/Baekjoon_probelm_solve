# 문제번호: 2581
# 소수의 합과 최소값 구하기
# url: https://www.acmicpc.net/problem/2581
# 출처: 나의 네이버 블로그 (blog.naver.com/ydonchoi83)
# 2022.06.19.~2022.07.01.

#########################
# [문제]
# 자연수 M과 N이 주어질 때 M이상 N이하의 자연수 중 소수인 것을 모두 골라,
# 이들 소수의 합과 최소값을 찾는 프로그램을 작성하시오.
#########################

# be about to revise soon... Below is a prior solution.


import random
def summary_all_primes_btw():
	m = random.randint(1, 100)
	n = random.randint(1, 100)
	print(f'{m}과 {n} 사이에 존재하는 소수는 ', end=' ')
	sieve = [False, False] + [True]*(n-1)
	primes = []
	if m < n:
		for i in range(m, n+1):
			if sieve[i]:
				primes.append(i)
				for j in range(i*2, n+1, i):
					sieve[j] = False
		print(primes)
		return print('*합: {}, *최소값: {}, *최대값: {}'.format(sum(primes), min(primes), max(primes)))
summary_all_primes_btw()


# fin.