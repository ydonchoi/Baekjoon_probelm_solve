#파이썬 #백준 #문제풀이 #12891번 #DNA비밀번호 #최영돈(231110,band.us/@ydonchoi)
'''
(문제)
DNA문자열: 모든 문자열에 등장하는 문자가 A, C, G, T 중 특정 문자들로 이루어진 문자열을 말한다.
임의의 DNA 문자열에서 부분문자열을 뽑아 비밀번호로 사용하려 한다.
이때 비밀번호는 사용자가 정한 규칙(특정 문자열의 등장 횟수)에 따른다.
임의의 DNA 문자열과 비밀번호로 사용할 부분문자열의 길이, 그리고 사용자 규칙이 주어질때
만들 수 있는 비밀번호 종류의 수를 구하는 프로그램을 작성하시오.
단, 부분문자열이 동일하더라도 등장 위치가 다르다면 다른 것으로 취급한다.
첫번째 줄에는 임의의 DNA 문자열과 부분문자열의 길이가 출력된다.
두번째 줄에는 임의의 DNA 문자열이 주어진다.
세번쨰 줄에는 사용자 규칙(등장횟수)이 주어진다.
'''


def count_passwords(s, m):
    n = len(s)
    count = 0
    start = 0
    end = 1
    
    while end <= n:
        cnt = [0] * 4
        for i in range(start, end):
            cnt[ord(s[i]) - ord('A')] += 1
            
        if all(cnt[i] >= m[i] for i in range(4)):
            count += 1
        start = end
        end += 1
        
    return count

def main():
    s = input()
    m = list(map(int, input().split()))
    print(count_passwords(s, m))

if __name__ == "__main__":
    main()
