# 문제번호: 1193
# 분수 찾기
# url: https://www.acmicpc.net/problem/1193
# 출처: 나의 네이버 블로그 (blog.naver.com/ydonchoi83)
# 2022.06.19.~2022.07.01.
# revise: 2024. 06. 18.

#########################
## (문제)
# 무한히 큰 배열에 다음과 같이 분수들이 적혀있다.
# 1/1 1/2 1/3 1/4 1/5 …
# 2/1 2/2 2/3 2/4 …   …
# 3/1 3/2 3/3 …   …   …
# 4/1 4/2 …   …   …   …
# 5/1 …   …   …   …   …
# …   …   …   …   …   …
# 이와 같이 나열된 분수들을 1/1 → 1/2 → 2/1 → 3/1 → 2/2 → … 과 같은 지그재그 순서로 차례대로 1번, 2번, 3번, 4번, 5번, … 분수라고 하자.
# X가 주어졌을 때, X번째 분수를 구하는 프로그램을 작성하시오.
#########################

''' (approach)
1. 나열된 분수의 지그재그 순서에는 일정한 패턴이 존재
2. 지그재그 순서의 터닝 포인트에서 1/분모 -> 분자/1 -> 1/분모 -> 분자/1 순으로 번갈아 나타남
3. 1로 시작하는 곳에서는 +1, 분자 또는 분모에서 시작하는 곳에서는 -1이 되며, 합계는 변화 없음
4. 터닝 포인트부터 지그재그 이동 횟수는 분자 또는 분모와 같음
'''

# My Solution_revised (24.06.18.)
def sum_of_numbers(num: int) -> int:
    return int(num*(num+1)/2)

def gen_fraction(num: int) -> int:
    new_num = num - 1
    fraction = [f'{1+i}/{new_num-i}' for i in range(new_num)]
    return fraction if new_num % 2 == 0 else fraction[::-1]

def main():
	number = int(input('input number: '))
	idx = 0
	while sum_of_numbers(idx) < number:
		idx += 1
	move = number - sum_of_numbers(idx)
	fraction_list = gen_fraction(idx+1)
	print(fraction_list[move-1])

if __name__ == '__main__':
	main()

# fin.