# 문제번호: 17219
# 비밀번호 찾기
# url: https://www.acmicpc.net/problem/17219
# 23.11.03.
# updated: 24.06.15.

##################################################
# (문제)
# 2019 HEPC-MAVEN League의 '비밀번호 만들기'와 같은 방식으로 비밀번호를 만든 경민이는 하나의 문제점을 발견했다.
# 그 문제점은 비밀번호가 랜덤으로 만들어져서 기억을 못한다는 것이다.
# 그래서 사이트 주소와 비밀번호를 메모장에 적어두고 필요할 때마다 찾아서 사용하였다.
# 이를 본 문석이가 경민이를 위해 메모장에서 비밀번호를 찾아주는 프로그램을 만들어주려고 한다.
# 비밀번호를 찾으려는 사이트 주소의 비밀번호를 차례대로 하나씩 각 줄에 출력하시오.
# 
# (조건)
# 첫째 줄에는 저장된 사이트 주소의 개수 N(1<=N<=100,000)과 비밀번호를 찾으려는 사이트 주소의 수 M(1<=M<=100,000)이 주어진다.
# 둘째 줄부터 각 줄에는 사이트 주소와 비밀번호가 공백으로 구분되어서 주어진다.
# 사이트 주소는 알파벳 소문자/대문자, 대시, 마침표로 이루어져 있으며 중복되지 않는다.
# 비밀번호는 알파벳 대문자로만 이루어져 있다. 길이는 모두 최대 20자이다.
# N+2 번째 줄부터 M개의 줄에 걸쳐 비밀번호를 찾으려는 사이트 주소가 한 줄에 하나씩 입력된다. 이때, 반드시 이미 저장된 사이트 주소가 입력된다.
##################################################


# My solution_revised (24. 06. 15.)

def search_PW(storage: dict, key: str) -> str:
    ''' search stored password via site address return stored password.
    if not exist, return whether store new password or not.'''

    if not storage.get(key):
        Q = input('No password. Do you generate and store new random password? (y/n)').lower()
        return Q
    return storage.get(key)


def gen_random_PW(num: int) -> str:
    '''generates password mixed by upper and lower letters returns random password expressed string type'''
    
    length = num
    string_pool = string.ascii_letters
    password = ''.join(random.choice(string_pool) for _ in range(length))
    return password


def store_PW(storage: dict, new_site: str) -> dict:
    '''stores new password returns whole stored site addresses and passwords'''

    num = int(input('wanna generate the length of new random password: '))
    new_password = gen_random_PW(num)
    storage[new_site] = new_password
    return storage


def main():
    # 아직 실력이 부족한지.. storage를 별도로 관리하려고 해봤는데.. 동기화시키는 것 못해서 신규 pw는 저장이 안됨 ㅠ
    # 그냥 storage 별도 관리하는 건 포기...ㅠ.ㅠ
    storage = {
    'www.abc.kr':'ABCKR',
    'www.korea.kr':'KOREA',
    'www.coding.kr':'CODING',
    'www.computer.kr':'COMKR',
    'www.Sam-Sung.kr':'SAM'
    }
    
    test = int(input('whole test number: '))
    cnt = 0
    while cnt < test:
        search_site = input('input site address searching password: ')
        check_password = search_PW(storage, search_site)
        if check_password == 'y':
            storage = store_PW(storage, search_site)
        else:
            cnt += 1
            print(f'URL: {search_site}, Password: {check_password}')
            

if __name__ == "__main__":
    import random
    import string
    main()


# Fin.