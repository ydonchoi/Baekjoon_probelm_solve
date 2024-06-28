# 문제번호: 2775
# 부녀회장이 될테야
# url: https://www.acmicpc.net/problem/2775
# 출처: 나의 네이버 블로그 (blog.naver.com/ydonchoi83)
# 2022.06.19.~2022.07.01.
# revised on 24. 06. 28.

#########################
# [문제]
# 평소 반상회에 참석하는 것을 좋아하는 주희는 이번 기회에 부녀회장이 되고 싶어, 각 층의 사람들을 불러 모아 반상회를 주최하려고 한다.
# 이 아파트에 거주를 하려면 조건이 있는데,
# “a층의 b호에 살려면 자신의 아래(a-1)층의 1호부터 b호까지 사람들의 수의 합만큼 사람들을 데려와 살아야 한다” 는 계약 조항을 꼭 지키고 들어와야 한다.
# 아파트에 비어있는 집은 없고 모든 거주민들이 이 계약 조건을 지키고 왔다고 가정했을 때, 주어지는 양의 정수 k와 n에 대해 k층에 n호에는 몇 명이 살고 있는지 출력하라.
# 단, 아파트에는 0층부터 있고 각층에는 1호부터 있으며, 0층의 i호에는 i명이 산다.
#########################

# revised on 24. 06. 28.
def gen_input(test: int) -> list[tuple]:
	return [(random.randint(1,10), random.randint(1,10)) for _ in range(test)]

def num_of_residents(floor: int, room: int):
    if floor == 1:
        return sum(range(1,room+1))
    if room == 1:
        return 1
    return residents(floor-1, room) + residents(floor, room-1)

def main():
	num = int(input('enter the num. of test:'))
	test = gen_input(num)
	cnt = 0
	for element in test:
		cnt += 1
		floor, room = map(int, element)
		residents = num_of_residents(floor, room)
		print(f"test{cnt} | the residents' number of {floor} floor {room} room is {residents}")

if __name__ == '__main__':
	import random
	main()

# fin.