# 문제번호: 2805
# 나무 자르기
# url: https://www.acmicpc.net/problem/2805
# 23.12.28

#########################
## (문제)
## N개의 나무들이 있다. 상근이는 N개의 나무들을 자르기 위해 높이를 조정할 수 있는 절단기를 가져왔다.
## 절단기로 나무를 잘라 총 길이가 M인 나무 조각들을 집으로 가져가려 한다.
## 이때 절단기 높이로 설정할 수 있는 높이 H의 최대값을 구하는 프로그램을 작성하시오.
## 
## (입력)  나무의 갯수(N), 집으로 가져갈 나무 길이(M)
## (출력)  절단기 높이(H)
#########################

def wood_cutter(wood, M):
    H = (sum(wood) - M) / len(wood)
    wood = [i if i >= H else 0 for i in wood]
    H = (sum(wood) - M) / (len(wood)-wood.count(0))
    return H

def main():    
    wood = random.sample(range(1, 100), int(input('나무 갯수')))
    M = int(input('가져갈 나무의 총 길이:'))
    H = wood_cutter(wood, M)
    print(H)

if __name__ == '__main__':
    import random
    main()
    

# fin.
