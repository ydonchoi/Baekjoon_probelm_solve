# 문제번호: 10250
# ACM 호텔
# url: https://www.acmicpc.net/problem/10250
# 출처: 네이버블로그(blog.naver.com/ydonchoi83)

# 2022.06.19. ~ 2022.07.01.
# revised: 2024.06.11.

###########################
# (문제)
# ACM 호텔 매니저는 손님이 도착하는 대로 빈 방을 배정하고 있다.
# 손님들은 호텔 정문으로부터 걸어서 가장 짧은 거리에 있는 방을 선호한다.
# 호텔 정문에서 걷는 거리가 가장 짧은 방을 배정하는 프로그램을 작성하시오.
# (가정)
# 문제를 단순화하기 위해 호텔은 직사각형이라고 가정한다.
# 각 층에는 W개의 방이 있는 H층 건물(H x W 형태)이라고 가정한다 (1 <= H, W <= 99)
# 인접한 두 객실 사이의 거리는 모두 동일(d=1)하며, 호텔 정면부에만 객실이 있다고 가정한다. (H=6, W=12인 가상의 호텔 건물 그림은 출처에서 직접 확인)
# 호텔 정문은 1층 엘리버이터 바로 앞에 있으며, 정문에서 엘리베이터까지 거리는 무시한다.
# 손님이 엘리베이터를 타고 이동하는 거리는 고려하지 않는다.
# 걸어서 이동하는 거리가 동일할 경우 아래층의 객실을 더 선호한다.
###########################


# My_solution_revised: 24. 06.11.
def generator(test: int) -> list:
    building = [(random.randint(1, 99) for _ in range(2)) for _ in range(test)]
    visitor = [random.randint(1, 99**2) for _ in range(test)]
    return building, visitor


def display(building: list, visitor: list, idx: int) -> list:
    H, W = map(int, building[idx])
    num = visitor[idx]
    return H, W, num


def assign_room(H: int, W: int, num: int) -> int:
    if num > int(H * W):
        return False
    if num % H == 0:
        j = H // W
        i = H
    else:
        j = H // W + 1
        i = num % H
    return f'{str(j)}0{str(i)}' if i < 10 else str(j)+str(i)


def main():
    T = int(input('전체 테스트 횟수(회): '))
    building, visitor = generator(T)
    for idx in range(len(building)):
        H, W, num = display(building, visitor, idx)
        print(f'\n건물 높이: {H}층\n각 층별 전체 객실 수: {W}개')
        if room := assign_room(H, W, num):
            print(f'{num}번째 투숙 인원이 투숙할 객실은 {room} 호입니다.')
        else:
            print('[투숙 불가] 수용가능인원을 초과하였습니다.')


if __name__ == "__main__":
    import random
    main()

# fin.
