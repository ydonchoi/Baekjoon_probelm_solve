#파이썬 #백준 #문제풀이 #1150번 #백업문제 #최영돈(문겸,20231013,band.us/@ydonchoi)
'''
(문제)
n개의 회사가 존재하며, 케이블이 k개 존재한다.
k개의 네트워크 케이블로 회사를 연결하려고 할때,
전체 네트워크 케이블 길이가 최소가 되는 경우를 구하는 프로그램을 작성하시오.
'''
# 문제 풀이 실패

# (정답 예제)
# 입력 받기
n, k = map(int, input().split()) # 회사 수와 케이블 수
s = [] # 회사의 위치를 저장할 리스트
for _ in range(n):
    s.append(int(input()))

# 회사들을 k 쌍으로 묶었을 때 필요한 케이블의 길이의 최솟값을 구하는 함수
def min_cable_length(k):
    # 이분 탐색을 위한 범위 설정
    left = 0 # 최소 케이블 길이
    right = s[-1] - s[0] # 최대 케이블 길이

    # 이분 탐색 반복
    while left <= right:
        mid = (left + right) // 2 # 중간 값
        count = 0 # 가능한 케이블 쌍의 수
        start = 0 # 시작 인덱스

        # 각 회사에 대해 반복
        for i in range(n):
            # 현재 회사와 시작 회사의 거리가 중간 값보다 크거나 같으면
            if s[i] - s[start] >= mid:
                count += 1 # 케이블 쌍의 수 증가
                start = i # 시작 인덱스 갱신

        # 가능한 케이블 쌍의 수가 k 이상이면
        if count >= k:
            left = mid + 1 # 최소 케이블 길이를 늘린다
        else: # 가능한 케이블 쌍의 수가 k 미만이면
            right = mid - 1 # 최대 케이블 길이를 줄인다

    return right # 최종적으로 구한 최대 케이블 길이 반환

# 결과 출력
print(min_cable_length(k))
