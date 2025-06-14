# 문제번호: 1712
# 손익 분기점
# url: https://www.acmicpc.net/problem/1712
# 출처: 나의 네이버 블로그 (blog.naver.com/ydonchoi83)
# 2022.06.19.~2022.07.01.

#########################
# [문제]
# 월드전자는 노트북을 제조하고 판매하는 회사이다.
# 노트북 판매 대수에 상관없이 매년 임대료, 재산세, 보험료, 급여 등 A만원의 고정 비용이 들며,
# 한 대의 노트북을 생산하는 데에는 재료비와 인건비 등 총 B만원의 가변 비용이 든다고 한다.
# 예를 들어 A=1,000, B=70이라고 하자. 이 경우 노트북을 한 대 생산하는 데는 총 1,070만원이 들며,
# 열 대 생산하는 데는 총 1,700만원이 든다. 노트북 가격이 C만원으로 책정되었다고 한다.
# 일반적으로 생산 대수를 늘려 가다 보면 어느 순간 총 수입(판매비용)이 총 비용(=고정비용+가변비용)보다 많아지게 된다.
# 최초로 총 수입이 총 비용보다 많아져 이익이 발생하는 지점을 손익분기점(BREAK-EVEN POINT)이라고 한다.
# A, B, C가 주어졌을 때, 손익분기점을 구하는 프로그램을 작성하시오.
#########################

# just modifies code expressions on prior's.. 24.06.19.


def get_revenue(price: int, fix_cost: int, var_cost: int, qty: int) -> int:
	return ((price-var_cost)*qty)-fix_cost


def main():
	price = int(input("sell_price: "))
	fix_cost = int(input("fix_cost: "))
	var_cost = int(input("var_cost: "))
	qty = 0
	while get_revenue(price, fix_cost, var_cost, qty) <= 0:
		qty += 1
	print('break-even point: ', qty)


if __name__ == "__main__":
	main()

# fin.
