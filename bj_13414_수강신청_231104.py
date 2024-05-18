#백준 #문제풀이 #13414번 #수강신청 #최영돈(231103,band.us/@ydonchoi)
'''
수강신청 부하 관리 시스템을 도입하려고 한다. 새로운 관리시스템의 작동방식은 다음과 같다.
1) 수강신청 버튼이 활성화된 후, 버튼을 조금이라도 빨리 누른 학생이 대기 목록에 먼저 들어간다.
2) 이미 대기열에 들어가있는 상태에서 다시 수강신청 버튼을 누르는 경우 대기목록의 맨 뒤로 밀려난다.
3) 잠시 후 수강신청 버튼이 비활성화되면,
대기목록에서 가장 앞에 있는 학생부터 자동으로 수강신청이 완료되며, 수강 가능 인원이 꽉찰 경우 나머지 대기 목록은 무시하고 수강신청을 종료한다.
입력 데이터는 표준 입력을 사용한다. 입력은 1개의 테스트 데이터로 구성된다.
첫째 줄에는 과목 수강 가능 인원 k(1<=k<=100,000)와 학생들이 버튼을 클릭한 순서로 기록한 대기목록 길이 L(1<=L<=500,000)이 주어진다.
둘째 줄부터는 수강신청 버튼을 클릭한 학생의 학년이 클릭 순서대로 주어진다.
학번은 8자리의 숫자로 이루어져 있다.
출력은 표준 출력을 사용한다.
입력 데이터에 대해, 수강신청 관리시스템 규칙 적용 이후 수강신청 성공 인원의 학번을 한 줄에 하나씩 출력한다.
'''
import random
# 수강가능인원수, 대기 학생 수 입력
n, k = map(int, input('대기 학생 수(n)와 수강가능인원 수(k):').split())
student_id = []
entry = []
print(f'최대 수강가능인원:{k}')
# 수강신청 버튼 활성화 되어 학생들이 버튼을 눌렀다는 가정
for _ in range(n):
    student_id.append(random.randint(10000000,100000000))
while True:
    button = int(input('버튼 클릭은 "1"을, 종료는 "2"를 입력'))
    if button == 2: break
    elif button != 1: pass
    else:
        if len(entry) < k:
            entry.append(student_id.pop(0))
        else: pass
print(f'전체 수강 인원: {len(entry)}')
for id in range(len(entry)): print(entry[id])  # fin.


'''
(모범답안1)
def solution(N, K, courses):
    applied = 0
    for i in range(len(courses)):
        if applied < K and courses[i] <= N:
            applied += 1
            courses[i] = -1
            return i + 1
    return -1

(모범답안2)
def solution(N, K, courses):
    courses.sort()
    for i in range(len(courses)):
        if courses[i] <= N:
            return i + 1
    return -1

N, K = map(int, input().split())
courses = list(map(int, input().split()))
print(solution(N, K, courses))

# 두 번째가 더 효율적임
'''