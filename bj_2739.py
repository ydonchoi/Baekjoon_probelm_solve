# 문제번호: 2739
# 구구단
# url: https://www.acmicpc.net/problem/2739
# 출처: 나의 네이버 블로그 (blog.naver.com/ydonchoi83)
# 2022.06.19.~2022.07.01.

#########################
# [문제]
# N을 입력받은 뒤, 구구단 N단을 출력하는 프로그램을 작성하시오.
# 출력 형식에 맞춰서 출력하면 된다. 출력형식과 같게 N*1부터 N*9까지 출력한다.
#########################

# be about to revise soon... Below is a prior solution.


N = input()
for i in range(1,10):
	tot = int(N)*i
	print('{} X {} = {}'.format(N,i,tot))


# fin.