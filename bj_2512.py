# 문제번호: 2512
# 예산배정
# url: https://www.acmicpc.net/problem/2512
# 23.12.29

#########################
# (문제)
# 국가의 역할 중 하나는 여러 지방의 예산 요청을 심사하여 국가 예산을 분배하는 것이다.
# 여러 지방의 예산 요청액과 국가의 예산 총액이 주어졌을 때, 여러 지방의 예산 요청액을 최대한 수용하여 분배하는 프로그램을 작성하시오.
# (입력) 여러 지방 N 곳의 개별 예산 요청액, 분배가능한 최대 국가 예산 총액(M)
# (출력) 여러 지방 중 최대로 배정된 예산액 : 정수로 출력(내림)
#########################


def distribution_budget(req_budget: int, tot_budget: int) -> int:
    distribution: int = tot_budget / len(req_budget)
    each_budget: list[int] = [min(i, distribution) for i in req_budget]
    residual: list[int] = [distribution - each_budget[k] for k in range(len(each_budget))]
    return (
        int(distribution + (sum(residual) / residual.count(0)))
        if residual.count(0) < len(residual)
        else distribution
    )


def main():
    each_budget: int = random.sample(range(1, int(input('지방정부 최대 요청 가능 예산액:'))), int(input('요청 지방정부 수:')))
    total_budget: int = int(input('분배가능한 최대 예산액'))
    result: int = distribution_budget(each_budget, total_budget)
    print(result)


if __name__ == '__main__':
    import random
    main()

# fin.
