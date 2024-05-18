#파이썬 #백준 #문제풀이 #2512번 #예산배정문제 #23.12.29 #최영돈(band.us@ydonchoi)
'''
(문제)
국가의 역할 중 하나는 여러 지방의 예산 요청을 심사하여 국가 예산을 분배하는 것이다.
여러 지방의 예산 요청액과 국가의 예산 총액이 주어졌을 떄,
여러 지방의 예산 요청액을 최대한 수용하여 분배하는 프로그램을 작성하시오.
(입력) 여러 지방 N 곳의 개별 예산 요청액, 분배가능한 최대 국가 예산 총액(M)
(출력) 여러 지방 중 최대로 배정된 예산액 : 정수로 출력(내림)
'''

def distribution_budget(req_budget, tot_budget):
    distribution = tot_budget / len(req_budget)
    each_budget = [i if i < distribution else distribution for i in req_budget]
    residual = [distribution - each_budget[k] for k in range(len(each_budget))]
    if residual.count(0) < len(residual):
        max_budget = int(distribution + (sum(residual) / residual.count(0)))
    else: max_budget = int(distribution)
    return print(max_budget)

def main():
    import random
    each_budget = random.sample(range(1, int(input('지방정부 최대 요청 가능 예산액:'))), int(input('요청 지방정부 수:')))
    total_budget = int(input('분배가능한 최대 예산액'))
    distribution_budget(each_budget, total_budget)
    
if __name__ == '__main__':
    main()

# fin.