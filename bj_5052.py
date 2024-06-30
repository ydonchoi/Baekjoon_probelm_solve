# 문제번호: 5052
# 전화번호 목록
# url: https://www.acmicpc.net/problem/5052
# 23.10.21.

#########################
# (문제)
# 주어진 전화번호의 목록에 일관성이 있는지를 구하는 프로그램을 작성하시오.
# 일관성이 있으려면 하나의 번호가 다른 번호의 접두어인 경우가 없어야 한다.
# (조건)
# 첫째 줄에는 테스트 케이스 수 t(1<=t<=50)가 주어진다.
# 각 테스트 케이스의 첫째 줄에는 전화번호의 수 n(1<=n<=10000)이 주어지고, 다음의 n개 줄에는 전화번호들이 주어진다.
# 전화번호의 길이는 길어야 10자리이며, 하나의 목록에서 동일한 전화번호는 없다.
#########################


def gen_tel_number_list(num: int) -> list[int]:
    return random.sample(range(1, 1000000), k=num)


def check_tel_number_list(num: int, tel: list[int]) -> list[bool]:
    check = []
    for i in range(num):
        for j in range(i+1, num):
            print(tel[i], tel[j])
            if str(tel[i]) == str(tel[j])[:len(str(tel[i]))]:
                check.append(False)
    return check


def main():
    T = int(input('테스트 횟수(50회 이하 입력):'))
    for _ in range(T):
        num = int(input('전화번호 갯수:'))
        tel = gen_tel_number_list(num)
        check = check_tel_number_list(num, tel)
        print('No') if len(check) > 0 else print('Yes')
        print("==="*10)


if __name__ == '__main__':
    import random
    main()

# fin.

# (모범답안1)
# def solution(S):
#     N = len(S)
#     for i in range(N):
#         if S[i] != S[N-i-1]:
#             return False
#     return True

# (모범답안2)
# def solution(S):
#     N = len(S)
#     return S[:N//2] == S[N//2:][::-1]

# T = int(input())
# for _ in range(T):
#     S = input()
#     print(solution(S))
