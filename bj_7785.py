# 문제번호: 7785
# 자료구조
# url: https://www.acmicpc.net/problem/7785
# 23.10.28.

#########################
# (문제)
# 회사 출퇴근 로그기록: 출입기록 (enter, leave)
# 첫 줄에는 출입기록 수 N 출력
# 다음 줄부터 사람 이름, 그리고 enter 또는 leave 출력
# 사람이름: 알파벳 대소문자로 이루어진 5글자 이하, 동명이인X, 대소문자가 다를 경우 다른 이름
# 현재 사무실에 있는 사람을 사전역순으로 출력
#########################


class CheckInOffice():

    def __init__(self, name=None):
        self.names = []
        self.name = name

    def records(self, name):
        if self.name not in self.names:
            print(self.name, 'enter')
            self.names.append(name)
        else:
            print(self.name, 'leave')
            self.names.remove(name)
        return self.names.sort(reverse=True)

    def main(self):
        T = int(input('Test(회):'))
        for _ in range(T):
            self.name = input('이름:')
            self.records(self.name)
        print(self.names)


if __name__ == '__main__':
    office = CheckInOffice()
    office.main()

# fin

# (모범답안1)
# def solution(logs):
#     now = int(input())
#     answer = []
#     for log in logs:
#         time, name = log.split()
#         time = int(time)
#         if time >= now:
#             answer.append(name)
#     return answer

# (모범답안2)
# def solution(logs):
#     now = int(input())
#     answer = set()
#     for log in logs:
#         time, name = log.split()
#         time = int(time)
#         if time <= now:
#             answer.remove(name)
#         else:
#             answer.add(name)
#     return list(answer)

# T = int(input())
# for _ in range(T):
#     logs = input().split()
#     print(solution(logs))
# 두 방법 모두 동일함
