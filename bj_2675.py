# 문제번호: 2675
# 문자열 반복
# url: https://www.acmicpc.net/problem/2675
# 출처: 나의 네이버 블로그 (blog.naver.com/ydonchoi83)
# 2022.06.19.~2022.07.01.

#########################
# [문제]
# 문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오.
# 즉, 첫번째 문자를 R번 반복하고, 두번째 문자를 R번 반복하는 식으로 P를 만들면 된다.
# S에는 QR Code "alphanumeric" 문자만 들어있다.
# QR Code "alphanumeric" 문자는 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./: 이다.
# 첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 1,000)가 주어진다.
# 각 테스트 케이스는 반복 횟수 R(1 ≤ R ≤ 8), 문자열 S가 공백으로 구분되어 주어진다.
# S의 길이는 적어도 1이며, 20글자를 넘지 않는다. 각 테스트 케이스에 대해 P를 출력한다.
#########################

# be about to revise soon... Below is a prior solution.


def sentence():
	import random
	alphanumeric = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./;'
	case = random.randint(1, 100)
	select = random.randint(1, 20)
	collect = []
	for n in range(case):
		tmp = []
		for m in range(select):
			pick = random.randint(0, 44)
			tmp.append(alphanumeric[pick])
		s = "".join(tmp)
		collect.append(s)
	rpt = random.randint(1, 8)
	print('* 새 문자열 반복 횟수 = ', rpt)
	for r in range(len(collect)):
		p = []
		for q in range(len(collect[r])):
			n_tmp = collect[r][q]*rpt
			p.append(n_tmp)
		pp = ''.join(p)
		print('케이스{}: 새 문자열은 "{}"'.format(r+1, pp))

sentence()

# fin.
