# 문제번호: 1920
# 수 찾기
# url: https://www.acmicpc.net/problem/1920
# 23.12.28

#########################
## # (문제) N개의 정수가 주어졌을 떄, X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.
## # (출력) X라는 정수가 존재하면 1을, 존재하지 않으면 0을 출력
## # (분류) 이분탐색(binarysearch)
#########################

def binarysearch(list, target):
    midNum = 0
    start = 0
    end = len(list)
    while start < end:
        midNum = (end+start)//2
        if target == int(list[midNum]):
            return 1
        elif target < int(list[midNum]):
            end = midNum
        else:
            start = midNum + 1
    return 0

def main():
    list = random.sample(range(1,int(input('범위 입력:'))), int(input('갯수 입력:')))
    list = sorted(list)
    Mytarget = int(input('찾으려는 정수 X 입력:'))
    result = binarysearch(list, Mytarget)
    print(result)

if __name__ == '__main__':
    import random
    main()

# fin.