#파이썬 #백준 #문제풀이 #2491번 #수열 #최영돈(231021,band.us/@ydonchoi)
'''
(문제)
0~9까지의 숫자로 이루어진 수열이 있음
그 수열 안에서 연속적으로 커지거나 작아지는 구간이 있는지를 찾아서,
그 구간의 길이가 가장 긴 구간 길이를 출력하시오.
(단, 연속 증가 또는 감소 구간 길이가 3 이상인 구간이 없을 경우 길이는 2로 출력)
'''
import random
import time

# 입력값이 양수인지 확인하는 함수
def is_positive(num):
    try:
        num = int(num)
        return num > 0
    except:
        return False

# 양수를 입력받는 함수
def input_positive(msg):
    num = input(msg)
    while not is_positive(num):
        print("양수를 입력해주세요.")
        num = input(msg)
    return int(num)

# 무작위로 숫자 수열을 생성하는 함수
def generate_num_seq(num_digits):
    num_seq = ""
    for i in range(num_digits):
        num_seq += str(random.randint(0,9))
    return num_seq

def mysolution(num_seq, N):
    max_length = 1
    for c in range(N-1):
        cnt = 1
        if num_seq[c] >= num_seq[c+1]:
            cnt += 1
            for d in range(c+1, N-1):
                if num_seq[d] >= num_seq[d+1]: cnt +=1
                else: break
        elif num_seq[c] <= num_seq[c+1]:
            cnt += 1
            for d in range(c+1, N-1):
                if num_seq[d] <= num_seq[d+1]: cnt +=1
                else: break
        if max_length <= cnt: max_length = cnt
    return max_length     # fin.
'''
(GPT의 코드 리뷰)
코드의 목적은 무작위로 생성된 숫자 수열에서 가장 긴 증가하거나 감소하는 부분 수열의 길이를 구하는 것으로 보입니다.
1. 코드의 가독성을 높이기 위해 변수의 이름을 의미있게 바꾸세요.
예를 들어, N은 num_digits, chr은 num_seq, length은 max_length, cnt은 cur_length 등으로 변경할 수 있습니다.
2. 코드의 효율성을 높이기 위해 반복문을 줄이세요.
현재 코드는 O(N^2)의 시간 복잡도를 가지는데, 이는 수열의 길이가 커질수록 많은 시간이 소요됩니다. 반복문을 한 번만 사용하여 O(N)의 시간 복잡도로 줄일 수 있습니다. 방법은 다음과 같습니다.
수열의 첫 번째 원소부터 마지막 원소까지 순서대로 탐색하면서, 현재 원소가 이전 원소보다 큰지 작은지를 판단합니다.
만약 현재 원소가 이전 원소보다 크다면, 증가하는 부분 수열의 길이를 1 증가시키고, 감소하는 부분 수열의 길이를 1로 초기화합니다.
만약 현재 원소가 이전 원소보다 작다면, 감소하는 부분 수열의 길이를 1 증가시키고, 증가하는 부분 수열의 길이를 1로 초기화합니다.
만약 현재 원소가 이전 원소와 같다면, 두 부분 수열의 길이를 모두 1로 초기화합니다.
각 경우마다, 증가하는 부분 수열의 길이와 감소하는 부분 수열의 길이 중 큰 값을 최대 길이와 비교하여 갱신합니다.
코드의 정확성을 높이기 위해 예외 상황을 처리하세요. 현재 코드는 입력값이 0이나 음수일 때 오류가 발생합니다. 이를 방지하기 위해 입력값이 양수인지 확인하고, 아니라면 다시 입력하도록 요청하세요.
'''
# GPT의 코드 수정 제안
# 가장 긴 증가하거나 감소하는 부분 수열의 길이를 구하는 함수
def find_max_length(num_seq):
    max_length = 1 
    inc_length = 1 
    dec_length = 1 
    for i in range(1, len(num_seq)):
        if num_seq[i] > num_seq[i-1]: 
            inc_length += 1 
            dec_length = 1 
        elif num_seq[i] < num_seq[i-1]: 
            dec_length += 1 
            inc_length = 1 
        else: 
            inc_length = 1 
            dec_length = 1
        max_length = max(max_length, inc_length, dec_length) 
    return max_length

# GPT 생성 모범답안1) 현재 숫자와 이전 숫자를 비교하여 결정하는 방법
# 아.. 이건 증가하는 경우만 포함되는 거구나 ㅋㅋ
def solution_1(num_seq, N):
    max_length = 0
    length = 1
    for i in range(N):
        if num_seq[i] >= num_seq[i-1]:
            length += 1
        else:
            max_length, length = 0, 1
        if length > max_length:
            max_length = length
    return max_length

# # GPT 생성 모범답안2) DP 테이블을 이용하여 저장하는 방법
# def solution_2(num_seq, N):
#     dp = [1 for _ in range(N)]
#     for i in range(1, N):
#         for j in range(i):
#             if num_seq[i] > num_seq[j] and dp[i] < dp[j] + 1:
#                 dp[i] = dp[j] + 1
#     return max(dp)

def main():
    num_digits = input_positive('몇 자리 수열을 생성하시겠습니까?:') 
    stime = time.time()
    num_seq = generate_num_seq(num_digits) # 숫자 수열을 생성함
    arr = list(num_seq)
    print(num_seq)
    m1time = time.time()
    print(f'{m1time-stime}초')
    max_length = mysolution(num_seq, len(num_seq))
    print(max_length) # 결과를 출력함
    m2time = time.time()
    print(f'{m2time-m1time}초')
    max_length = find_max_length(num_seq) # 최대 길이를 구함
    print(max_length) # 결과를 출력함
    m3time = time.time()
    print(f'{m3time-m2time}초')
    max_length = solution_1(num_seq, len(arr)) # 최대 길이를 구함
    print(max_length) # 결과를 출력함
    m4time = time.time()
    print(f'{m4time-m3time}초')
    # max_length = solution_2(num_seq, len(arr)) # 최대 길이를 구함
    # print(max_length) # 결과를 출력함
    # etime = time.time()
    # print(f'{etime-m4time}초')

'''
mysolution, find_max_length, solution_1의 결과 차이
일단 눈에 띄는 이유는
동일 값에 대해서
mysolution은 계속 증가 또는 감소로 인정해서 카운팅
find_max_length는 증가 또는 감소로 인정하지 않고 카운팅
solution_1은 증가하는 것만 카운팅
'''

if __name__=='__main__':
    main()