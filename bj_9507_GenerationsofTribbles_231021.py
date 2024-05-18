#백준 #문제풀이 #9507번 #GenerationsofTribbles #최영돈(231021,band.us/@ydonchoi)
'''
(문제)
꿍이는 기존의 피보나치보다 조금 더 복잡한 피보나치를 만들려고 한다.
꿍이 만든 이 피보나치 함수를 koongs(n)이라 할때,
n < 2: 1
n = 2: 2
n = 3: 4
n > 3: koongs(n-1)+koongs(n-2)+koongs(n-3)+koongs(n-4) 이다.
입력의 첫째 줄에는 전체 테스트 갯수(0<t<69)가 주어진다.
다음 t줄에는 몇 번째 피보나치를 구해야 하는지를 나타내는 n(0<=n<=67)이 주어진다.
각 테스트 케이스마다 꿍 피보나치 수를 출력하라.
'''
T = int(input('테스트 횟수 입력:'))
print(f'전체 테스트 횟수: {T}')
cnt = 0
while True:
    if T == cnt: break
    else:
        cnt+=1
        N = int(input('몇 번째 꿍스 피보나치 수를 출력하시겠습니까?'))
        if N >= 0:
            koongs = [1,1,2,4]
            if N > 3:
                for n in range(4,N+1):
                    k_피보 = koongs[n-1]+koongs[n-2]+koongs[n-3]+koongs[n-4]
                    koongs.append(k_피보)
            print(f'{N}번째 꿍스 피보나치 수: {koongs[N]}')
        else: print("error")  # fin.
        
'''
(모범답안1)
def solution(N):
    if N < 2:
        return N
    else:
        return solution(N-1) + solution(N-2)

(모범답안2)
def solution(N):
    dp = [0] * (N+1)
    dp[0], dp[1] = 0, 1
    for i in range(2, N+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[N]

T = int(input())
for _ in range(T):
    N = int(input())
    print(solution(N))

# 시간복잡도(2^N < N) 측면에서 재귀적인 방법보다 더 효율적임
'''