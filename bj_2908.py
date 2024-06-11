# 문제번호: 2908
# 상수의 숫자 읽기
# url: https://www.acmicpc.net/problem/2908
# 출처: 네이버 블로그(blog.naver.com/ydonchoi83)

# 22.06.19 ~ 22.07.01.
# revised: 24.06.11.

#########################
## (문제)
## 상근이의 동생 상수는 숫자를 다른 사람과 다르게 거꾸로 읽는다.
## 상근이는 상수에게 3자리 수 2개를 칠판에 써주었다.
## 그 다음 크기가 큰 수를 말해보라고 했다.
## 상수의 대답을 출력하는 프로그램을 작성하시오.
#########################

def two_number(num: int) -> int:
    num_1, num_2 = map(int, [random.randint(100, 1000) for _ in range(2)])
    return num_1, num_2

def read_number(num_1:int, num_2:int) -> int:
    num_1, num_2 = str(num_1), str(num_2)
    rv_num_1, rv_num_2 = int(num_1[::-1]), int(num_2[::-1])
    return rv_num_1, rv_num_2

def sangsu_answer(rv_num_1: int, rv_num_2: int) -> int:
    if rv_num_1 >= rv_num_2:
        return rv_num_1
    else:
        return rv_num_2

def main():
    T = int(input('test: '))
    for cnt in range(T):
        num_1, num_2 = two_number(cnt)
        read_num_1, read_num_2 = read_number(num_1, num_2)
        answer = sangsu_answer(read_num_1, read_num_2)
        print(f'칠판에는 {num_1}, {num_2}가 적혀 있습니다.')
        print(f'상근이는 {read_num_1}, {read_num_2}라고 읽습니다.')
        print(f'그리고 {answer}가 더 크다고 답합니다.')

if __name__ == "__main__":
    import random
    main()

# fin.