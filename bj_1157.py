# 문제번호: 1157
# 단어 공부
# url: https://www.acmicpc.net/problem/1157
# 출처: 나의 네이버 블로그 (blog.naver.com/ydonchoi83)
# 2022.06.19.~2022.07.01.
# revise 24.06.17.

##############################################
# [문제]
# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오.
# 단, 대문자와 소문자를 구분하지 않는다. 첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다.
# 주어지는 단어의 길이는 1,000,000을 넘지 않는다.
# 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다.
# 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.
##############################################

# My solution_revised(24.06.17.)
def check_alphabet(word: str) -> dict:
	''' checks alphabet appearance from word, and returns appearance number per alphabet '''
	checker = {alphabet: 0 for alphabet in string.ascii_lowercase}
	for alp in word:
		for k, v in checker.items():
			if alp == k:
				checker[k] += 1
	return checker

def word_list(num: int) -> list:
	words = [input('wanna check english word').lower() for _ in range(num)]
	return words

def sort_checker(checker: dict) -> dict:
	''' new dictionary sorted by value in ordered by descending '''
	sorting = sorted(checker.items(), key=lambda x: x[1], reverse=True)
	new_checker = {element[0]:element[1] for element in sorting}
	return new_checker

def main():
	test = int(input('whole trial num: '))
	words = word_list(test)
	for idx in range(len(words)):
		print('word is:', words[idx])
		checker = check_alphabet(words[idx])
		max_appearance = max(checker.values())
		max_appear = []
		for k, v in checker.items():
			if v != 0:
				print(f'{k}: {v}')
			if v == max_appearance:
				max_appear.append(k)
		print(f'the most: {max_appearance} 번')
		print(max_appear,'\n')

if __name__ == "__main__":
	import string
	main()

# fin.