# 문제번호: 25804
# Infinity Area
# url: https://www.acmicpc.net/problem/25804
# 24.01.03.

#########################
## (문제)
# R, A, B의 세 정수가 주어진다.
# 당신은 무한대 심볼의 중앙(S)에 위치해 있으며, 중앙(S)에서 먼저 오른쪽으로 반지름이 R인 원을 그린다. 그리고 중앙(S)에서 왼쪽으로 반지름이 (R x A)인 원을 그린다.
# 그 다음엔 다시 중앙(S)에서 오른쪽으로 반지름이 (R x A / B)인 원을 그린다.
# 그 다음에 다시 중앙(S)에서 왼쪽으로 반지름이 (R x A / B x A)인 원을 그린다.
# 동일한 방식으로 중앙(S)을 지나는 무한대 기호를 그라는 작업을 반지름이 0이 될 때까지 반복한다.
# 반지름이 0이 될때까지, 생선된 원의 전체 넓이(the sum of areas of all the circles)를 구하시오.
#########################

# '''
# (solution)
# - 무한대의 반지름을 구하고, 각 반지름에 해당하는 원의 넓이를 구하여 합한다.
# - 무한대 심볼은 오른쪽 원을 그리는 것으로 시작하여, 왼쪽 원을 그리는 것으로 끝난다.
# - 계산의 편의를 위해 pi는 3.14로 한다.
# '''


def radius_list(r,a,b):
    radius = [r]
    idx = 0
    while radius[idx] > 0:
        idx += 1
        if idx % 2 == 0:
            if radius[idx-1]//b != 0:
                radius.append(radius[idx-1]//b)
            else: break
        else:
            radius.append(radius[idx-1]*a)
    return radius


def Inf_symbol_area(r,a,b):
    area = [3.14*(k**2) for k in radius_list(r,a,b)]
    return sum(area)


def main():
    r, a, b = map(int, input('자연수 3개:').split())
    sum_area = Inf_symbol_area(r,a,b)
    print(sum_area)


if __name__=='__main__':
    main()