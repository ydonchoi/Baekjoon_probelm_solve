#백준 문제풀이 #1920번(수 찾기) #이분탐색(binarysearch) #23.12.28 #최영돈(band.us@ydonchoi)
# (문제) N개의 정수가 주어졌을 떄, X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.
# (출력) X라는 정수가 존재하면 1을, 존재하지 않으면 0을 출력

def binarysearch(list, target):
    midNum = 0
    start = 0
    end = len(list)
    while start < end:
        midNum = (end+start)//2
        if target == int(list[midNum]):
            return print('1')
        elif target < int(list[midNum]):
            end = midNum
        else:
            start = midNum + 1
    return print('0')

def main():
    import random
    list = random.sample(range(1,int(input('범위 입력:'))), int(input('갯수 입력:')))
    list = sorted(list)
    Mytarget = int(input('찾으려는 정수 X 입력:'))
    binarysearch(list, Mytarget)

if __name__ == '__main__':
    main()

# fin.