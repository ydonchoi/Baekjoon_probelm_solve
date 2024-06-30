# 문제번호: 1010
# 다리놓기
# url: https://www.acmicpc.net/problem/1010
# 23.10.19.

#########################
# (문제)
# 한 도시를 가로지는 강을 두고 강의 서쪽과 강의 동쪽을 연결하는 다리를 놓으려고 한다.
# 서쪽의 사이트와 동쪽의 사이트를 연결하는 조건은 다음과 같다.
# 1. 하나의 사이트는 하나의 다리만 연결할 수 있다.
# 2. 강의 서쪽보다 강의 동쪽이 더 많은 사이트를 가지고 있다.
# 최대한 많은 다리를 놓으려고 할때, 다리를 지을 수 있는 경우의 수를 구하는 프로그램을 작성하시오.
#########################

'''(solution)
- 서쪽과 동쪽이 일대일 대응되는 함수로 생각
- 동쪽의 사이트가 서쪽의 사이트보다 더 많기 때문에, 경우의 수는 조합으로 풀이
- => 동쪽 combination 서쪽 으로 solution 작성
'''


def solution_1(W: int, E: int):
    return comb(E, W)


def comb(n: int, r: int) -> int:
    return 1 if r == 0 or n == r else comb(n-1, r-1) + comb(n-1, r)


def comb_with_factorial(n: int) -> int:
    return 1 if n == 0 else n * comb_with_factorial(n-1)


def solution_2(W: int, E: int) -> float:
    return int(comb_with_factorial(E) / (comb_with_factorial(W)*comb_with_factorial(E-W)))


def main():
    W, E = map(int, input('서쪽(W), 동쪽(E) 입력 (W < E):').split(' '))
    print(f'solution_1: {solution_1(W, E)}')
    print(f'solution_2: {solution_2(W, E)}')


if __name__ == "__main__":
    main()
