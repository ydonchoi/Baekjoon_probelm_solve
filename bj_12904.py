# 문제번호: 12904
# A와B
# url: https://www.acmicpc.net/problem/12904
# 23.10.22.

#########################
## (문제)
## A와 B로만 이루어진 영어 단어들이 있다. 이를 이용해서 간단한 게임을 만들고자 한다.
## 두 문자열 S와 T가 주어졌을때, S를 T로 바꾸는 게임이다.
## 문자열을 바꿀 때는 다음의 2가지 연산만 가능하다.
## 1) 문자열 뒤에 A를 추가한다.
## 2) 문자열을 뒤집어 뒤에 B를 추가한다.
## 주어진 조건을 이용해서 S를 T로 만들 수 있는지 없는지를 알아내는 프로그램을 작성하시오.
## 
## (조건)
## 첫째 줄에 S가, 둘째 줄에는 T가 주어진다. (1<=S길이<=999, 2<=T길이<=1000, S길이<T길이)
## S를 T로 바꿀 수 있으면 1을, 없으면 0을 출력한다.
#########################

# My_solution_revised(24.06.08.)
def gen_characters(S_num: int, T_num: int) -> list:
    S = ''.join(random.choice(['A','B']) for _ in range(S_num))
    T = ''.join(random.choice(['A','B']) for _ in range(T_num))
    return S, T

def conv_deco(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return wrapper

def compute_1(S):
    return S + 'A'

def compute_2(S):
    return S[::-1] + 'B'

def compute_3(S):
    S += 'A'
    return S[::-1] + 'B'

@conv_deco
def converting(S: str, T:str):
    idx = len(S)-1
    if S == T[idx]:
        return compute_1(S)
    if S[::-1] == T[idx]:
        return compute_2(S)
    else:
        return compute_3(S)

@conv_deco
def judge_convertable(S: str, T:str):
    while len(S) < len(T):
        S = converting(S, T)
        if S != T[:len(S)]:
            return 0
    return 1
    
def main():
    Test = int(input('Test: '))
    S_num, T_num = map(int, input('the nuber of characters of S and T (S < T): ').split())
    if S_num >= T_num:
        print("T's number should be more greater than S's")
    cnt = 0
    while cnt < Test:
        cnt += 1
        S, T = gen_characters(S_num, T_num)
        res = judge_convertable(S, T)
        if res == 1:
            print(f'cnt: {cnt}', S, T)

if __name__ == "__main__":
    import random
    main()

# fin.




# ''' another solutions with ChatGPT

# (solution_1)
# def solution(S):
#     cnt = 0
#     for i in range(len(S)-1, -1, -1):
#         if S[i] == "A":
#             cnt += 1
#         elif S[i] == "B":
#             cnt -= 1
#         if cnt == 0:
#             return len(S)-i-1
#     return -1

# (solution_2)
# def solution(S):
#     cntA = 0
#     cntB = 9
#     for c in S:
#         if c == "A":
#             cntA += 1
#         elif c == "B":
#             cntB += 1
#     return min(cntA, cntB)

# T = int(input())
# for _ in range(T):
#     S = input()
#     print(solution(S))

# ''' between two, it says 2nd solution is more efficient.