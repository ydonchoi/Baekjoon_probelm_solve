# 백준 문제(1110번): 더하기 사이클 문제 (https://www.acmicpc.net/problem/1110)_최영돈(문겸)
while True:
    num = int(input('100 이하의 수 입력:'))
    tmp, cnt = str(num), 0
    if num == 0 : 
        print('탈출! yeap!')
        break
    elif len(str(num)) < 2:
        print('100 이하의 두 자리 수를 다시 입력하세요.')
        pass        
    elif len(str(num)) >= 3:
        print('100 이하의 두 자리 수를 다시 입력하세요.')
        pass        
    else:
        while True:
            a, b = tmp[0],tmp[1]
            cnt +=1
            tmp = str(int(a)+int(b))
            if int(tmp) >= 10: tmp = tmp[1]
            tmp = str(b)+str(tmp)
            if num == int(tmp):
                print(f'더하기 싸이클: {cnt}회')
                break

# 풀이2 (작년에 풀었던 풀이 방식)_지난 작업물 보다가 발견함
N = int(input())
cnt=0
if N//10 == 0:
    N *= 10
NN = 10*(N%10)+((N//10)+(N%10))%10
while True:
    cnt+=1
    if NN == N:
        break
    else:
        NN = 10*(NN%10)+((NN//10)+(NN%10))%10
        print(NN)
print(f'cnt:{cnt}')