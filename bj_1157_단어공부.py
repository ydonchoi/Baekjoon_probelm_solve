# #파이썬 #백준 
# #1157번문제 #단어공부문제

# - 출처: 나의 네이버 블로그 (blog.naver.com/ydonchoi83)
# - 기간: 2022.06.19.~2022.07.01.

# [문제]
# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다. 첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다. 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.

def pop_word():
	word = input()
	alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	alp_num = []
	for i in range(len(alphabet)):
		cnt = 0
		for j in range(len(word)):
			if alphabet[i] == word[j]:
				cnt += 1
		alp_num.append(cnt)
		print(alphabet[i], '등장횟수: {} 회'.format(cnt))
	for k in range(len(alp_num)):
		if alp_num[k] == max(alp_num):
			max_alpha = alphabet[k]
			print('* 가장 많이 사용된 알파벳: ', max_alpha.upper())  # 하나인 경우 대문자 출력
			# 여러 개인 경우 출력은?  pass!

pop_word()

# 다음 복기 때 더 심플한 아이디어가 떠오르면 추가 작성하기!
# 등장하지 않는 알파벳은 제거, pass한 것(여러 개인 경우 출력?)도 포함하기! 순서 변경(가장 많이 등장한 알파벳 제일 먼저 출력하기)


# fin.