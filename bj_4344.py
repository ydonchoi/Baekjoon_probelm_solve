# 문제번호: 4344
# 평균은 넘겠지
# url: https://www.acmicpc.net/problem/4344
# 출처: 나의 네이버 블로그 (blog.naver.com/ydonchoi83)
# 2022.06.19.~2022.07.01.

#########################
# [문제]
# 대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다.
# 당신은 그들에게 슬픈 진실을 알려줘야 한다.
# 첫째 줄에는 테스트 케이스의 개수 C가 주어진다.
# 둘째 줄부터 각 테스트 케이스마다 학생의 수 N(1 ≤ N ≤ 1000, N은 정수)이 첫 수로 주어지고, 이어서 N명의 점수가 주어진다.
# 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.
# 각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 반올림하여 소수점 셋째 자리까지 출력한다.
#########################


# be about to revise soon... Below is a prior solution.

import random
case = input('케이스 수:')
for c in range(1, int(case)+1):
	score_list = []
	score_upper = []
	num = random.randint(1,1000)
	for i in range(int(num)):
		r = random.randint(1,100)
		score_list.append(r)
	aver = sum(score_list)/int(len(score_list))
	for k in range(int(len(score_list))):
		if score_list[k] > aver:
			score_upper.append(score_list[k])
	print('(케이스{}) - 학급 평균 점수를 상회하는 학생의 비율: {}%'.format(c, round(len(score_upper)/num*100, 3)))

	
# fin.