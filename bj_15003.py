# 문제번호: 15003
# Amsterdam Distance
# url: https://www.acmicpc.net/problem/15003
# 24.01.03. ~ 24.01.05.

#########################
## (문제)
# 암스테르담 거리는 반지름이 r인 반원 형태의 길로 구성되어 있다. 암스테르담 거리 한 곳(A)에서 다른 곳(B)으로 이동하는 최단 거리를 구하라.
# 첫번째 줄에는 세 정수(M, N, R)가 주어진다.
# - R(실수): 전체 반원의 반지름 길이 // M(정수): 반원의 중앙에서 세로로 구획하는 구획 수 // N(정수): 반원의 중앙으로부터 가로로 구획하는 구획 수
# 두번째 줄에는 A 장소(n1,m1)와 B 장소(n2,m2)가 차례대로 주어진다. 이 때, A에서 B로 가는 최단 거리를 구하시오.
#########################


'''
(solution)
- N이 작을수록 M1과 M2 간의 거리가 짧아진다.
- N으로의 이동: abs(n1-n2)
- M으로의 이동: lm = (2*3.14*radius_n*min(m1,m2)) * (theta/360)
- 계산의 편의상 pi는 3.14로 함
- 따라서 N 좌표에서의 이동 후, M 좌표에서의 이동을 하는 것을 최단 거리로 계산
'''


def AmsterdamDistance(M,N,R,n1,m1,n2,m2):
    radius_n = R / N
    theta = 180 / M
    lm = ((2*3.14*radius_n)*min(m1,m2)) * (theta/360)
    return radius_n*(abs(m1-m2)) + (lm*(abs(n1-n2)))

def main():
    M, N, R = map(int, input('거리의 세로와 가로 구획 수(M, N), 반지름(R) 입력:').split(' '))
    m1, n1 = map(int, input('A장소(m1,n1)의 좌표 입력:').split(' '))
    m2, n2 = map(int, input('B장소(m2,n2)의 좌표 입력:').split(' '))
    if n1 <= (N+1) and n2 <= (N+1) and m1 <= (M+1) and m2 <= (M+1):
        print(f'세로구획:{M}, 가로구획:{N}, 반지름:{R}\nA:({m1},{n1}) -> B:({m2},{n2})')
        dist = AmsterdamDistance(M,N,R,m1,n1,m2,n2)
        print(f'거리: {dist}')
    else:
        print(f'장소는 {M+1, N+1}보다 크지 않아야 합니다.')
  
if __name__ == "__main__":
    main()


# fin.
