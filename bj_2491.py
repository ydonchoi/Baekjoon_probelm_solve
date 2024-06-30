# 문제번호: 2491
# 수열
# url: https://www.acmicpc.net/problem/2491
# 23.10.21.
# revised_24.06.16.

##################################################
# (문제)
# 0~9까지의 숫자로 이루어진 수열이 있음
# 그 수열 안에서 연속적으로 커지거나 작아지는 구간이 있는지를 찾아서, 그 구간의 길이가 가장 긴 구간 길이를 출력하시오.
# (단, 연속 증가 또는 감소 구간 길이가 3 이상인 구간이 없을 경우 길이는 2로 출력)
##################################################

''' increase_length와 decrease_length가 중복되는 형태라서, 조금 더 간소화하고 싶다..ㅠ '''


# My solution_revised(24.06.16.)
def gen_progression(num: int) -> str:
    ''' creates sequence of numbers from inputting number '''
    progression = str(random.randint(1, 9)) + ''.join([str(random.randint(0, 9)) for _ in range(num-1)])
    if progression[0] == '0':
        progression[0] = str(random.randint(1, 9))
    return progression


def increase_length(progression: str) -> int:
    ''' searches numbers greater than prior number and returns length '''
    inc_length = 0
    length = 1
    ind = 0
    while ind < len(progression)-1:
        ind += 1
        if progression[ind-1] < progression[ind]:
            length += 1
        else:
            if inc_length <= length:
                inc_length = length
            length = 1
    return inc_length


def decrease_length(progression: str) -> int:
    ''' searches numbers greater than prior number and returns length '''
    dec_length = 0
    length = 1
    ind = 0
    while ind < len(progression)-1:
        ind += 1
        if progression[ind-1] > progression[ind]:
            length += 1
        else:
            if dec_length <= length:
                dec_length = length
            length = 1
    return dec_length


def compare_res(inc_length: int, dec_length: int) -> int:
    ''' compares numbers with incresing max length and decreasing max length
    and returns max length '''
    res = max(inc_length, dec_length)
    return 2 if res < 3 else res


def main():
    test = int(input("whole test's trial number: "))
    num = int(input('How many digits do you want to create?: '))
    for _ in range(test):
        progression = gen_progression(num)
        inc_length = increase_length(progression)
        dec_length = decrease_length(progression)
        print(f'gen_lenght: {len(progression)} | gen_seq: {progression} | result: {compare_res(inc_length, dec_length)}')


if __name__ == "__main__":
    import random
    main()

# fin.
