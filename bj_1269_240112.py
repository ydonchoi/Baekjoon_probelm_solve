# 문제번호: 1269
# 대칭 차집합
# url: https://www.acmicpc.net/problem/1269
# 23.11.03. / 24.01.12.

##############################################
## <My_Solution>_init_231103
## def donnysolution(a,b,A,B):
##     A.extend(B)
##     union = list(set(A))
##     intersection = []
##     for i in range(a):
##         for j in range(b):
##             if A[i] == B[j]: intersection.append(A[i])
##     print(len(union)-len(intersection))
##############################################

# GPT 생성 모범 답안 1_엄청 간단하게 푸네 헤헤
def solution_1(A,B):
    union = A | B
    intersection = A & B
    return len(union), len(intersection), len(union)-len(intersection)

# GPT 생성 모범 답안 2_엄청 간단하게 푸네 헤헤
def solution_2(A, B):
    A_set = set(A)
    B_set = set(B)
    return len(A_set|B_set), len(A_set&B_set), len(A_set|B_set)-len(A_set&B_set)

def main():
    import random
    T = int(input('테스트횟수:'))
    for t in range(T):
        trial = input('집합 자동 생성(0 입력) 또는 집합 직접 입력(1 입력):')
        if trial == str(0):
            a, b = map(int, input('a,b 원소 갯수(100개 미만):').split())
            K = set(random.sample(range(101), k=a))
            L = set(random.sample(range(101), k=b))
            print(t+1,a,b), print(len(K)), print(K), print(len(L)), print(L)
            print('solution_1: ',solution_1(K,L))
        elif trial == str(1):
            A = list(map(int, input('a원소입력:').split()))
            B = list(map(int, input('b원소입력:').split()))
            print(t+1), print(len(A)), print(B), print(len(A)), print(B)
            print('solution_2: ',solution_2(A,B))
        else: print(f'{t+1}번째 테스트는 실패')
        
if __name__=='__main__':
    main()

