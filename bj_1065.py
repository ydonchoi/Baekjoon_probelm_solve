# 문제번호: 1065
# 한수
# url: https://www.acmicpc.net/problem/1065
# 출처: 나의 네이버 블로그 (blog.naver.com/ydonchoi83)
# 2022.06.19.~2022.07.01.

#########################
## (문제)
# 어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다.
# 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다.
# N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오.
# 첫째 줄에 1,000보다 작거나 같은 자연수 N이 주어진다.
#########################

# be about to revise.. below is a prior solution.

''' (approach) [풀이과정 구상]
한수라는 개념이 어떤 수 X가 주어졌을 때, 각 자리 수가 등차수열을 이루는 수를 말한다? 그러면 최소한 세자리 이상인 수라는 전제가 있어야. 그러면 최소 자연수는 100부터 시작.
제시된 조건에 따르면 1000보다 작거나 같은 자연수가 주어지므로, 입력가능한 자연수는 세자리 자연수로 한정하고 공차의 범위는 최소 1부터 최대 4까지로 잡은 다음, 이를 기반으로 한수를 출력하는 기본함수 만들고 랜덤 수 입력하여 한수로 구성된 리스트를 산출하여 한수 개수 출력하는 프로그램 구현'''

def equiv_num(num):
	result = []
	for i in range(1,num):
		d = int(((i%100)//10)-(i%10))
		if d == 0: pass
		else:
			if i < 100: pass
			elif 100 <= i <= 1000:
				if ((i//100)-(i%10)) == 2*d:
					result.append(i)
				else: pass
			elif 1000 <= i <= 10000:
				if ((i//1000) - (i%10)) == 3*d:
					result.append(i)
				else: pass
			else: pass
	return print('산출된 한수의 갯수 = {}개\n산출된 한수 목록: {}'.format(len(result),result))

import random
num = random.randint(1,10000)
print('입력된 자연수(랜덤) = ', num)
equiv_num(num)
print()
print('complete')


# fin.