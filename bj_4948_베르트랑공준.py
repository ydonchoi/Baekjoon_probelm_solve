# #파이썬 #백준 
# #4948번문제 #베르트랑공준문제
# - 출처: 나의 네이버 블로그 (blog.naver.com/ydonchoi83)
# - 기간: 2022.06.19.~2022.07.01.

# [문제]
# #베르트랑 공준 문제
# 베르트랑 공준은 임의의 자연수 n에 대하여, n보다 크고, 2n보다 작거나 같은 소수는 적어도 하나 존재한다는 내용을 담고 있다. 이 명제는 조제프 베르트랑이 1845년에 추측했고, 파프누티 체비쇼프가 1850년에 증명했다.
# 자연수 n이 주어졌을 때, n보다 크고, 2n보다 작거나 같은 소수의 개수를 구하는 프로그램을 작성하시오.

# 문제가 어려워서 검색하여 찾아본 내용
def Bertrand(m):
	sieve = [False, False] + [True]*(2*m-1)
	primes_all = []  # 전체 요소 리스트
	primes_blw = []  # 예외 요소 리스트
	for i in range(1, 2*m+1):
		if sieve[i]:
			primes_all.append(i)
			for j in range(i*2, 2*m+1, i):
				sieve[j] = False
	for k in range(1, m+1):
		if sieve[k]:
			primes_blw.append(k)
			for l in range(k*2, m+1, k):
				sieve[l] = False
	# 전체 요소 리스트에서 에외 요소 리스트 제거하기
	primes = [a for a in primes_all if not a in primes_blw or primes_blw.remove(a)]
	return print(primes)

Bertrand(10)

# fin.