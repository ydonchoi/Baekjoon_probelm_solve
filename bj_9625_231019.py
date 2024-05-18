# 문제번호: 9625
# BABBA
# url: https://www.acmicpc.net/problem/9625
# 23.10.19.

###########################
## (문제)
## 기계의 화면에는 A만 표시되어 있다.
## 버튼을 1번 누르면 글자가 B로 변하고, 다시 1번 더 누르면 BA로 변한다.
## 다시 1번 더 누르면 BAB로, 그 다음에는 BABBA로 변한다.
## 상근이는 버튼을 누르면 화면의 모든 B는 BA로, A는 B로 바뀐다는 사실을 알게 되었다. 
###########################

'''
(문제해결)
k=1: A -> B
k=2: B -> BA
k=3: BA -> BAB
k=4: BAB -> BABBA
...
k=10: A는 34개, B는 55개 출력됨
* 문자열 대체 문제
'''

# init version
out = 'A'
k = int(input('버튼을 누를 횟수(회):'))
for _ in range(k):
    temp = ''
    for i in range(len(out)):
        if out[i] == 'A': temp += 'B'
        else:
            temp += 'BA'
    out = temp
print(out)   


# fin.



# '''
# (모범답안1)
# def solution(K):
#     a = 1
#     b = 0
#     for _ in range(K):
#         a, b = b, a + b
#     return a, b

# (모범답안2)
# def solution(K):
#     return (F(K+1)-F(K))//2
# def F(N):
#     if N <= 2:
#         return N
#     return F(N-1) + F(N-2)

# T = int(input())
# for _ in range(T):
#     K = int(input())
#     print(solution(K))
# '''

