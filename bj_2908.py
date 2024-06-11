# 문제번호: 2908
# 상수의 숫자 읽기
# url: https://www.acmicpc.net/problem/2908
# 출처: 네이버 블로그(blog.naver.com/ydonchoi83)

# 22.06.19 ~ 22.07.01.
# revised: 24.06.11.

#########################
## (문제)
## 상근이의 동생 상수는 숫자를 다른 사람과 다르게 거꾸로 읽는다.
## 상근이는 상수에게 3자리 수 2개를 칠판에 써주었다.
## 그 다음 크기가 큰 수를 말해보라고 했다.
## 상수의 대답을 출력하는 프로그램을 작성하시오.
#########################

import random
def read_num(s):
    num = []
    for i in range(s):
        for j in range(3):
            num.append(str(random.randint(1,9)))
        num.append("".join(num[i:]))
        del num[i:i+3]
    print(f'칠판에 적힌 숫자는 총 {s}개 입니다.')
    for m in range(len(num)):
        print("{}번째 숫자는 {}이며, 상근이는 {}이라고 읽습니다.".format(m+1, num[m], num[m][::-1]))

# 문) 칠판에 제시된 숫자는 총 20개입니다.
read_num(20)
