# 문제번호: 13414
# 수강신청
# url: https://www.acmicpc.net/problem/13414
# 23.11.03.

#########################
## (문제)
## 수강신청 부하 관리 시스템을 도입하려고 한다. 새로운 관리시스템의 작동방식은 다음과 같다.
## 1) 수강신청 버튼이 활성화된 후, 버튼을 조금이라도 빨리 누른 학생이 대기 목록에 먼저 들어간다.
## 2) 이미 대기열에 들어가있는 상태에서 다시 수강신청 버튼을 누르는 경우 대기목록의 맨 뒤로 밀려난다.
## 3) 잠시 후 수강신청 버튼이 비활성화되면,
## 대기목록에서 가장 앞에 있는 학생부터 자동으로 수강신청이 완료되며, 수강 가능 인원이 꽉찰 경우 나머지 대기 목록은 무시하고 수강신청을 종료한다.
## 입력 데이터는 표준 입력을 사용한다. 입력은 1개의 테스트 데이터로 구성된다.
## 첫째 줄에는 과목 수강 가능 인원 k(1<=k<=100,000)와 학생들이 버튼을 클릭한 순서로 기록한 대기목록 길이 L(1<=L<=500,000)이 주어진다.
## 둘째 줄부터는 수강신청 버튼을 클릭한 학생의 학년이 클릭 순서대로 주어진다.
## 학번은 8자리의 숫자로 이루어져 있다.
## 출력은 표준 출력을 사용한다.
## 입력 데이터에 대해, 수강신청 관리시스템 규칙 적용 이후 수강신청 성공 인원의 학번을 한 줄에 하나씩 출력한다.
#########################

# My_sloution_revised(24.06.06.)
def gen_student_id(num: int) -> list:
    return [random.randint(10000000, 100000000) for _ in range(num)]

def wait_list(student_id: list, wait: list) -> list:
    wait.append(student_id.pop(0))
    return wait

def button_click(student_id: list, wait: list) -> list:
    button_count = 0
    print("# plz press 1 button less than the number of wait_num #")
    while True:
        #수강신청 버튼 입력 상황 가정
        press_button = int(input('Press number 1 if participate, or Press number 0 if stop.'))
        button_count += 1
        print(f"Press num 1 counting: {button_count}")

        if press_button == 0:
            return waiting
        if press_button != 1:
            continue
        else:
            waiting = wait_list(student_id, wait)

def enroll(wait_list: list, num: int) -> list:
    return wait_list[:num]

def main():
    # 전체 참여 인원, 수강 가능 인원 입력
    wait_num = int(input('whole_waiting_students_num: '))
    enroll_num = int(input('in_class_num: '))
    student_id = gen_student_id(int(wait_num*2))
    wait = []
    waiting = button_click(student_id, wait)
    enroll_list = enroll(waiting, enroll_num)
    for student_id in enroll_list:
        print(student_id)


if __name__ == "__main__":
    import random
    main()

# fin.


# '''
# (모범답안1)
# def solution(N, K, courses):
#     applied = 0
#     for i in range(len(courses)):
#         if applied < K and courses[i] <= N:
#             applied += 1
#             courses[i] = -1
#             return i + 1
#     return -1

# (모범답안2)
# def solution(N, K, courses):
#     courses.sort()
#     for i in range(len(courses)):
#         if courses[i] <= N:
#             return i + 1
#     return -1

# N, K = map(int, input().split())
# courses = list(map(int, input().split()))
# print(solution(N, K, courses))

# # 두 번째가 더 효율적임
# '''