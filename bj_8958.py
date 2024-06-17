# 문제번호: 8958
# OX
# url: https://www.acmicpc.net/problem/8958
# 출처: 나의 네이버 블로그 (blog.naver.com/ydonchoi83)
# 2022.06.19.~2022.07.01.

#########################
# [문제]
# OX 퀴즈의 결과가 있다.
# O는 문제를 맞은 것이고, X는 문제를 틀린 것이다.
# 문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수가 된다.
# 예를 들어, 10번 문제의 점수는 3이 된다.
# "OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점이다.
# OX퀴즈의 결과가 주어졌을 때, 점수를 구하는 프로그램을 작성하시오.
#########################


# be about to revise soon if there is... Below is a prior solution.


result = "OOXXXXXXXOOOOOOXXXOXOXXXXOOX"
score = 0
for i in range(len(result)):
	if result[i] == "O": score += 1
print(f'획득한 점수는 {score} 점입니다.')


# fin.