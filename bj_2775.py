# 문제번호: 2775
# 부녀회장이 될테야
# url: https://www.acmicpc.net/problem/2775
# 출처: 나의 네이버 블로그 (blog.naver.com/ydonchoi83)
# 2022.06.19.~2022.07.01.

#########################
# [문제]
# 평소 반상회에 참석하는 것을 좋아하는 주희는 이번 기회에 부녀회장이 되고 싶어, 각 층의 사람들을 불러 모아 반상회를 주최하려고 한다.
# 이 아파트에 거주를 하려면 조건이 있는데,
# “a층의 b호에 살려면 자신의 아래(a-1)층의 1호부터 b호까지 사람들의 수의 합만큼 사람들을 데려와 살아야 한다” 는 계약 조항을 꼭 지키고 들어와야 한다.
# 아파트에 비어있는 집은 없고 모든 거주민들이 이 계약 조건을 지키고 왔다고 가정했을 때, 주어지는 양의 정수 k와 n에 대해 k층에 n호에는 몇 명이 살고 있는지 출력하라.
# 단, 아파트에는 0층부터 있고 각층에는 1호부터 있으며, 0층의 i호에는 i명이 산다.
#########################


# be about to revise soon... Below is a prior solution.

'''(approach)
아래에서 작성한 코드는, 주어진 문제로부터 "아파트의 시작이 1층부터 설정하였다는 점"이 차이가 있음'''

import random
T = random.randint(1, 10)
APT = []
for k in range(T):
	tmp = []
	for i in range(2):
		tmp.append(random.randint(1, 10))
	APT.append(tmp)
print(f'전체 테스트 횟수: {T}회')
for m in range(len(APT)):
	H, W = map(int, APT[m])
	print(f'\n아파트 높이: {H}층\n층별 전체 호수: {W}개')
	lst_w = []
	tmp = []
	a = 0
	for x in range(W):
		a += 1
		tmp.append(a)
	lst_w.append(tmp)
	for y in range(1, H):
		b = [1,]
		lst_w.append(b)
	for r in range(1, W):
		for q in range(1, H):
			lst_w[q].append(lst_w[q][-1]+lst_w[q-1][r])
	h = random.randint(1, H)
	w = random.randint(1, W)
	print(f'{h}동 {w}호에 거주하는 거주민 수는 {lst_w[h-1][w-1]}명입니다.')


# fin.