#백준 #문제풀이 #2491번 #수열 #최영돈(231021, @ydonchoi)
'''
0~9까지의 숫자로 이루어진 수열이 있음
그 수열 안에서 연속적으로 커지거나 작아지는 구간이 있는지를 찾아서,
그 구간의 길이가 가장 긴 구간 길이를 출력하시오.
(단, 연속 증가 또는 감소 구간 길이가 3 이상인 구간이 없을 경우 길이는 2로 출력)
'''

import random
N = int(input('몇 자리 수열을 생성하시겠습니까?:'))
length, chr = 2, ''
for i in range(N):
    chr += str(random.randint(0,9))
for c in range(N-1):
    cnt = 1
    if chr[c] >= chr[c+1]:
        cnt += 1
        for d in range(c+1, N-1):
            if chr[d] >= chr[d+1]: cnt +=1
            else: break
    elif chr[c] <= chr[c+1]:
        cnt += 1
        for d in range(c+1, N-1):
            if chr[d] <= chr[d+1]: cnt +=1
            else: break
    if length <= cnt: length = cnt
print(chr, length)


# fin.