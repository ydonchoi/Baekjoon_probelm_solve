#백준 #문제풀이 #17219번 #비밀번호찾기 #최영돈(231103,band.us/@ydonchoi)
'''
2019 HEPC-MAVEN League의 '비밀번호 만들기'와 같은 방식으로 비밀번호를 만든 경민이는 하나의 문제점을 발견했다.
그 문제점은 비밀번호가 랜덤으로 만들어져서 기억을 못한다는 것이다.
그래서 사이트 주소와 비밀번호를 메모장에 적어두고 필요할 때마다 찾아서 사용하였다.
이를 본 문석이가 경민이를 위해 메모장에서 비밀번호를 찾아주는 프로그램을 만들어주려고 한다.

첫째 줄에는 저장된 사이트 주소의 개수 N(1<=N<=100,000)과 비밀번호를 찾으려는 사이트 주소의 수 M(1<=M<=100,000)이 주어진다.
둘째 줄부터 각 줄에는 사이트 주소와 비밀번호가 공백으로 구분되어서 주어진다.
사이트 주소는 알파벳 소문자/대문자, 대시, 마침표로 이루어져 있으며 중복되지 않는다.
비밀번호는 알파벳 대문자로만 이루어져 있다. 길이는 모두 최대 20자이다.
N+2 번째 줄부터 M개의 줄에 걸쳐 비밀번호를 찾으려는 사이트 주소가 한 줄에 하나씩 입력된다.
이때, 반드시 이미 저장된 사이트 주소가 입력된다.
비밀번호를 찾으려는 사이트 주소의 비밀번호를 차례대로 하나씩 각 줄에 출력하시오.
'''
# 추가 부분: 사이트 주소 입력 및 비번 저장 여부 확인. 없으면 pass (문제 제시X)
# __init_version__
import random
storage = {
    'www.abc.kr':'ABCKR',
    'www.korea.kr':'KOREA',
    'www.coding.kr':'CODING',
    'www.computer.kr':'COMKR',
    'www.Sam-Sung.kr':'SAM'
    }
Q = input('랜덤 비밀번호를 저장할 사이트 주소가 있습니까?(Y/N)').upper()
if Q == 'Y':
    address = input("사이트 주소:")
    n = random.choice(range(10,21))
    pw = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    PW = random.choice(pw)
    for _ in range(n-1):
        PW += random.choice(pw)
    storage[address] = PW
# 제시된 문제 풀이
print(len(storage.keys()), len(storage.values()))
for i in range(len(storage)):
    print(list(storage.keys())[i], list(storage.values())[i])
print('\n아래는 검색 결과입니다\n')
while True:
    search = input('찾으려는 사이트 주소 입력:')
    if search == '': break
    elif search not in list(storage.keys()): print('다시 입력해주세요')
    else:
        print(search)
        for site in list(storage.keys()):
            if search == site: url = site
        print(storage[url])  # fin.