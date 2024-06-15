# 문제번호: 5525
# IOI
# url: https://www.acmicpc.net/problem/5525
# 23.10.22.
# revise_ 24.06.15.

##################################################
# (문제)
# N+1개의 I와 N개의 O로 이루어져 있으면, I와 O이 교대로 나오는 문자열을 PN이라고 한다.
# P1 IOI
# P2 IOIOI
# P3 IOIOIOI
# PN IOIOI...OI (O가 N개)
# I와 O로만 이루어진 문자열 S와 정수 N이 주어졌을 때, S안에 PN이 몇 군데 포함되어 있는지 구하는 프로그램을 작성하시오.
##################################################

'''
(approach)
1. start point에서 I와 O가 교대로 나오는 문자열을 탐색한다
2. 교대로 출현하는 길이(len(PN)를 구하고, PN에서 O의 개수를 센다 -> PN
3. 종료된 시점으로 start point를 옮긴 후, 다시 1번과 2번 과정을 반복한다.
4. 탐색 indicator가 S 문자열 끝에 도착하면 종료한다.
'''

# My solution_revised(24.06.15.)
# 테스트가 안되어서 우선 저장하고 테스트 확인 후, 계속 수정할 예정.

start = 0
indicator = 'IO'
idx = 0
PN = []
S = 'IIOIIIIIOOIIIIIOIIIIIOIOIOIIIIOIIOIIOOOOOIIIIOOOIOOOIOIOOOOOIOIOIIIOIOOOOIOOOIOIOOIIIOOIOII'
while idx < len(S):
    if S[idx:idx+2] == indicator:
        idx += len(indicator)
    else:
        if (idx-start) > 1:
            PN.append(S[start:idx])
            start = idx
            idx += 1

print(len(PN))

# fin.