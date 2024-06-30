# 문제번호: 5615
# 아파트임대
# url: https://www.acmicpc.net/problem/5615
# 23.05.17.

#########################
## (문제)
## 동규 부동산에서는 아파트를 임대하고 있는데, 아파트의 방은 면적이 2xy+x+y (x, y > 0)임
## 동규 부동산의 카탈로그에는 아파트 면적이 오름차순으로 적혀 있으며, 일부는 있을 수 없는 크기의 아파트도 적혀 있음
## 있을 수 없는 크기의 아파트를 임대하려고 하면, 동규는 "꽝!"이라고 외치면서 수수료만 떼어감
## 동규 부동산의 카탈로그에서 아파트 면적이 주어질 떄, 있을 수 없는 아파트의 수를 구하는 프로그램을 작성하시오.
#########################

def create_rental_catalogue(num:int) -> list[int]:
    return [random.randint(100, 10000) for _ in range(num)]

def is_able_to_rent(area_list:list[int]) -> dict:
    recieve_to_rent = {}
    for area in area_list:
        for x in range(1, area):
            if (area-x) % (2*x+1) == 0:
                recieve_to_rent[area] = (x, (area-x)/(2*x+1))
    return recieve_to_rent

def is_unable_to_rent(area_list:list, recieve_to_rent:dict) -> int:
    unable_to_recieve = 0
    for area in area_list:
        if area in recieve_to_rent.keys():
            print(f"'{area}' is an apartment rentable.")
        else:
            unable_to_recieve += 1
            print(f'"{area}" is 꽝(Boom)!!')

    return unable_to_recieve
        
def main():
    nums = int(input('아파트 수:'))
    area_list = create_rental_catalogue(nums)
    print(f'rental catalogue:\n{area_list}\n')
    able_to_rent = is_able_to_rent(area_list)
    unable_to_recieve = is_unable_to_rent(area_list, able_to_rent)
    print(f'\n있을 수 없는 아파트 면적의 수: {unable_to_recieve}')

if __name__ == '__main__':
    import random
    main()

# fin.