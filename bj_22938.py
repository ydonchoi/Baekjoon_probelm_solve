# 문제번호: 22938
# 백발백중하는명사수
# url: https://www.acmicpc.net/problem/22938
# 24.01.03

#########################
# (문제)
# 첫번째 줄에는 첫번째 과녁 중심 X1, Y1, 그리고 반지름 R1이 주어진다.
# 두번째 줄에는 두번째 과녁 중심 X2, Y2, 그리고 반지름 R2가 주어진다.
# X1, X2, X3, X4는 모두 정수이며, R1, R2는 모두 자연수이다.
# 두 과녁이 겹치면 YES를, 아니면 NO를 출력한다.
# 단, 한 점에서 만나는 경우는 겹치지 않는 것으로 생각한다.
#########################

'''(solution)
두 과녁(원)이 겹치지 않으려면 두 원의 중심 간 거리가 두 원의 반지름 합보다 작지 않아야 한다.
'''


def between_circles(x1: int, y1: int, x2: int, y2: int) -> int:
    return ((x2**2-x1**2)+(y2**2-y1**2))**(0.5)


def main():
    x1, y1, r1 = map(int, input('첫번째 과녁 중심과 반지름 입력(x1,y1,r1):').split())
    x2, y2, r2 = map(int, input('두번째 과녁 중심과 반지름 입력(x2,y2,r2):').split())
    if between_circles(x1, y1, x2, y2) < r1 + r2:
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()

# fin.
