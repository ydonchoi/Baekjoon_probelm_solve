# 문제번호: 17609
# 회문
# url: https://www.acmicpc.net/problem/17609
# 23.11.06.
# 23.11.07._init_version
# 24.01.07._revison_version: 전체 코드 정리 및 similar_symmetry_sen 함수 일부 수정

#########################
# (문제)
# 주어진 문자열이 회문인지, 유사회문인지, 일반문자열인지를 판단하는 프로그램을 작성하시오.
# 문자열의 개수는 30개 이내로 입력한다.
# 입력되는 문자열은 한 줄에 하나씩 출력한다.
# 주어진 문자열은 3개 이상, 100,000개 이하이며, 영문 알파벳 소문자로 구성된다.
# 각 줄마다 해당 문자열을 판단하여 0, 1, 2를 출력한다.
#########################

'''
(풀이소감) 와 진심 어려웠다..ㅠ 내가 푼 무식한 방법보다 더 쉬운 간단한 방법이 있겠지만..뭐..ㅎㅎㅎ
(궁금증)
여기서 even과 odd를 한번에 수행할 수 있는 방법은 없을까? (다른 간단한 방법으로 작성하면 고민할 필요도 없던데..)
입력 텍스트 중 '기러기러기기'는 유사회문으로, '기러기러기'와 '기기러기기' 모두 해당됨.
이런 경우 가능한 모든 유사회문이 출력되는 방법은 어떻게 수정하면 될까?
'''


def even_symmetry_sen(txt: str) -> str:
    forward = txt[:(len(txt)//2)]
    backward = txt[:(len(txt)//2)-1:-1]
    if forward == backward:
        print(txt, ':', 0)
    else:
        similar_symmetry_sen(txt)


def odd_symmetry_sen(txt: str) -> str:
    forward = txt[:(len(txt)//2)]
    backward = txt[:(len(txt)//2):-1]
    if forward == backward:
        print(txt, ':', 0)
    else:
        similar_symmetry_sen(txt)


def similar_symmetry_sen(txt: str):
    txt_re = txt
    for k in range((len(txt_re)//2)+1):
        if txt_re[k] != txt_re[-k-1]:
            if txt_re[k+1] == txt_re[-k-1]:
                txt_re = txt_re.replace(txt_re[k], '', 1)
                break
            elif txt_re[k] == txt_re[-k-2]:
                txt_re = txt_re.replace(txt_re[-k-1], '', 1)
                break
    if txt_re[:(len(txt_re)//2)] == txt_re[:(len(txt_re)//2):-1]:
        print(txt, '|', txt_re, ':', 1)
    else:
        print(txt, ':', 2)


def main():
    txt = ['abba', 'summuus', 'xabba', 'xabbay', 'comcom', 'comwwmoc', 'comwwtmoc', '우영우', '아야야아', '그리스', '스위스', '고무고무', 'abca', 'comcmo', '기러기러기기']
    for item in txt:
        if len(item) % 2 == 0:
            even_symmetry_sen(item)
        else:
            odd_symmetry_sen(item)


if __name__ == '__main__':
    main()

# fin.
