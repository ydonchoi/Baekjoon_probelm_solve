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

def create_lent_catalogue(num):
    area_list = [int(input('임대면적:')) for _ in range(num)]
    return area_list

def is_able_to_rent(area_list):
    lentable_catalogue = {}
    for area in area_list:
        for x in range(1, area):
            if int((area-x)/(2*x+1)) > 0:
                lentable_catalogue.update({area: (x, int((area-x)/(2*x+1)))})
    return lentable_catalogue

def lent_apartment(area_list, lentable_catalogue):
    unable_to_lent = 0
    for area in area_list:
        if not area in lentable_catalogue.keys():
            unable_to_lent += 1
            print('꽝!!')
        else:
            print("this is an apartment to lent. would you lent?")
    return unable_to_lent
        
def main():
    nums = int(input('아파트 수:'))
    area_list = create_lent_catalogue(nums)
    lentable_catalogue = is_able_to_rent(area_list)
    unable_to_lent = lent_apartment(area_list, lentable_catalogue)
    print(f'있을 수 없는 아파트 면적의 수: {unable_to_lent}')

if __name__ == '__main__':
    main()

# fin.