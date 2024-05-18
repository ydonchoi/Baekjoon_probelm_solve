# 문제번호: 4358
# 생태학
# url: https://www.acmicpc.net/problem/4358
# 23.11.05.

#########################
## (문제)
## 나무 이름은 최대 30글자 이내로 입력한다.
## 나무 종류는 최대 10,000그루 이내로 입력한다.
## 나무 수는 최대 1,000,000그루 이내로 입력한다.
## 이때 사전순으로 나무 종별로 출력하고, 각 종별 비율을 소수점 넷째 자리까지 입력한다.
#########################

def enrollment() -> bool:
    add = input('데이터를 등록하겠습니까?(Y/N)').upper()
    return True if add == 'Y' else False

def add_tree(tree: dict[str]) -> dict[str]:
    k, v = map(str, input('추가할 나무 종류와 이름 순서로 입력해주세요(30글자 이내):').split())
    if k not in list(tree.keys()):
        tree[k] = []
    tree[k].append(v)
    return tree

def confirm_data(tree: dict[str]) -> None:
    k_sort = sorted(tree)
    print(f'현재 등록된 데이터는 {len(tree.values())}개입니다.')
    for key in k_sort:
        print(key, round(len(list(tree[key]))/len(list(tree.values())),4))
    
def main():
    tree = {}
    while enrollment():
        tree = add_tree(tree)
        confirm_data(tree)

if __name__ == '__main__':
    main()

    
# fin.



# '''
# (모범답안1)
# def solution(N):
#     trees = set()
#     for tree in input().split():
#         trees.add(tree)
#     return round(len(trees) / 100, 4)

# (모범답안2)
# def solution(N):
#     trees = input().split()
#     return round(trees.count(" ") / (N-1), 4)

# T = int(input())
# for _ in range(T):
#     N = int(input())
#     print(solution(N))
# '''
