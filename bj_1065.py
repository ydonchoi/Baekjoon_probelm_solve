# 문제번호: 1065
# 한수
# url: https://www.acmicpc.net/problem/1065
# 출처: 나의 네이버 블로그 (blog.naver.com/ydonchoi83)
# 2022.06.19.~2022.07.01.
# revised on 2024.07.18.

#########################
## (문제)
# 어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다.
# 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다.
# N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오.
# 첫째 줄에 1,000보다 작거나 같은 자연수 N이 주어진다.
#########################

''' (solution)
- 3자리 수에서 각 자리 숫자가 등차수열을 이루는 경우, 2번째 자리 숫자는 산술평균값과 같다.
- 예를 들어, “147”은 [1, 4, 7]이므로 공차가 3인 등차수열이다. 이때 1번째 자리 숫자인 4와 3번째 자리 숫자인 7을 평균한 값이 2번째 자리 숫자인 4가 된다.
    → (1+7) / 2 = 8/2 = 4
- 따라서 한수를 구하는 문제는 이러한 등차수열의 특징을 이용한다.

- (심화) 주어진 조건 100 ≤ N ≤ 1,000을 넘어서는 경우에 한수를 구하는 프로그램도 나중에 시간될 때 작성해보자.
→ 이를 응용하여, 주어지는 자연수의 자리 수가 3자리, 4자리, 5자리일 때, 한수를 구하는 프로그램을 구해보자.
→ (주의) 예를 들어, 4자리 수가 주어질 때 “4826”이 한수라고 나오는 경우, 4 → 8 → 2 → 6은 등차수열이 아니므로 한수가 아니다.
'''

# (심화) 자리수를 고려하여 한수를 구하는 프로그램으로 기능 update_24.07.18

# 주어진 자연수까지 존재하는 전체 한수를 구하는 함수
def equiv_num(num):
    res = []
    for n in range(100, num+1):
        n_to_str = str(n)
        idx = 0
        while len(n_to_str) - idx > 2:
            check_n = n_to_str[idx:idx+3]
            if checker(check_n) == True:
                idx += 1
            else:
                idx = len(n_to_str)
        if idx == (len(n_to_str)-2):
            res.append(n)
    return res


# 한수 여부 확인하는 함수
def checker(check_n):
    return int(check_n[1]) == (int(check_n[0]) + int(check_n[2]))/2


# 주어진 자연수까지 존재하는 한수의 갯수와 한수 목록 출력
def main():
    num = random.randint(100,100000)
    print('입력된 자연수(랜덤) = ', num)
    result = equiv_num(num)
    print('산출된 한수의 갯수 = {}개\n산출된 한수 목록:\n{}'.format(len(result),result))


if __name__ == "__main__":
    import random
    main()


# fin.
