# 문제번호: 2577
# 숫자 개수 구하기
# url: https://www.acmicpc.net/problem/2577
# 출처: 나의 네이버 블로그 (blog.naver.com/ydonchoi83)
# 2022.06.19.~2022.07.01.
# revised_24. 06. 17.

#########################
# (문제)
# 세 개의 자연수 A, B, C가 주어질 때 A × B × C를 계산한 결과에서
# 0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지를 구하는 프로그램을 작성하시오.
# 예를 들어 A = 150, B = 266, C = 427 이라면 A × B × C = 17037300 이 되고,
# 계산한 결과 17037300 에는 0이 3번, 1이 1번, 3이 2번, 7이 2번 쓰였다.
# A, B, C는 모두 100보다 크거나 같고, 1,000보다 작은 자연수이다.
#########################


# My solution_revised(24.06.17.)
def num_counter(number: int) -> dict:
	''' the counter is that keys are composed to numbers from 0 to 9
	and values are composed to all 0, in order to counting from 0 to 9
	and returns initial dictionary type '''

	counter = {f'{key}': 0 for key in range(10)}
	for num in number:
		for k in counter:
			if k == num:
				counter[k] += 1
	return counter


def generate_number() -> str:
	''' generate each number A, B, and C, and multiply given three numbers A, B,
	and C, and returns computing result '''
	A, B, C = map(int, [str(random.randint(1, 9)) + ''.join([str(random.randint(0, 9)) for _ in range(2)]) for _ in range(3)])
	return str(A*B*C)


def main():
	number = generate_number()
	counter = num_counter(number)
	for key, value in counter.items():
		if value != 0:
			print(f'{key}: {value}번 등장')


if __name__ == "__main__":
	import random
	main()

# fin.
