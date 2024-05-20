# 문제번호: 10211
# Maximum Subarray
# url: https://www.acmicpc.net/problem/10211
# 23.12.03.

###########################
## (문제)
## 크기 N인 정수형 배열 X가 있을 때, X의 부분 배열(X의 연속한 일부분) 중 각 원소의 합이 가장 큰 부분 배열을 찾는 Maximum subarray problem(최대 부분배열 문제)은 컴퓨터 과학에서 매우 잘 알려져 있다.
## 여러분은 N과 배열 X가 주어졌을 때, X의 maximum subarray의 합을 구하라. 즉, max1 ≤ i ≤  j ≤ N (X[i]+...+X[j])를 구하라.
## 입력 파일의 첫 번째 줄에 테스트 케이스의 수를 의미하는 자연수 T가 주어진다. 그 다음에는 T개의 테스트 케이스가 주어진다.
## 각 테스트케이스 별로 첫 번째 줄에 배열의 크기 N이 주어진다. (1 ≤ N ≤ 1,000) 그리고 두 번째 줄에 배열 X의 내용을 나타내는 N개의 정수가 공백으로 구분되어 주어진다.
## 이때 주어지는 수는 절댓값이 1,000보다 작은 정수이다.
###########################


def Max_subarray(x):
    x_list = list(np.arange(1,x+1))
    return 2**len(x_list)-1

def main():
    x = int(input())
    Max_subarray(x)

if __name__ == "__main__":
    import numpy as np
    main()

    
# fin.
