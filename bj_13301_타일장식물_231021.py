#백준 #문제풀이 #13301번 #타일장식물 #최영돈(231021,band.us/@ydonchoi)
'''
(문제)
타일 장식물은 정사각형의 타일이다.
한변의 길이가 1인 정사각형 타일로 시작하여 앵무조개의 나선 모양처럼 점점 큰 타일을 붙인 형태로 이루어져있다.
타일의 한 변의 길이 순서는 [1,1,2,3,5,8,13...]순으로 이루어진다.
n개의 타일로 구성된 직사각형의 둘레를 구하는 프로그램을 작성하시오.
(해결방안)
피보나치 점화식 이용
'''
N = int(input('몇 개의 타일로 구성하시겠습니까?:'))
타일한변길이 = [1,1]
if N <= 2:
    pass
else:
    for n in range(2, N+1):
            temp = 타일한변길이[n-2] + 타일한변길이[n-1]
            타일한변길이.append(temp)
print(타일한변길이)
print('직사각형 둘레의 길이={}'.format(2*타일한변길이[N-1]+4*타일한변길이[N]))  # fin.


'''
(모범답안1)
def solution(N):
    dp = [0] * (N+1)
    dp[1], dp[2] = 1, 1
    for i in range(3, N+1):
        dp[i] = dp[i-1] + dp[i-2]
    return 2 * (dp[N-1]+dp[N])

(모범답안2)
def solution(N):
    return 2 * (F(N+1)-F(N))
def F(N):
    if N <= 2:
        return N
    return F(N-1) + F(N-2)

T = int(input())
for _ in range(T):
    N = int(input())
    print(solution(N))

# 두 번째가 더 효율적임
'''