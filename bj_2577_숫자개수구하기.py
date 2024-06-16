# #파이썬 #백준 
# #2577번문제 #숫자새수구하기문제

# - 출처: 나의 네이버 블로그 (blog.naver.com/ydonchoi83)
# - 기간: 2022.06.19.~2022.07.01.

# [문제]
# 세 개의 자연수 A, B, C가 주어질 때 A × B × C를 계산한 결과에 0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지를 구하는 프로그램을 작성하시오. 예를 들어 A = 150, B = 266, C = 427 이라면 A × B × C = 150 × 266 × 427 = 17037300 이 되고, 계산한 결과 17037300 에는 0이 3번, 1이 1번, 3이 2번, 7이 2번 쓰였다. A, B, C는 모두 100보다 크거나 같고, 1,000보다 작은 자연수이다.

# 이거 간략하게 만들고 싶은데.. 지금은 딱히 방법이 떠오르지 않음
import random
A = 100*random.randint(1,9)+10*random.randint(0,9)+random.randint(0,9)
B = 100*random.randint(1,9)+10*random.randint(0,9)+random.randint(0,9)
C = 100*random.randint(1,9)+10*random.randint(0,9)+random.randint(0,9)
print(A*B*C)
conv = str(A*B*C)
cnt = [0,0,0,0,0,0,0,0,0,0]
for i in range(10):
	for l in range(len(conv)):
		if int(conv[l]) == i:
			cnt[i] += 1
	if cnt[i] != 0:
		print('계산 결과, 숫자 {}는 {}번 사용되었습니다.'.format(i, cnt[i]))


# fin.