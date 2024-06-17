# 문제번호: 5622
# 할머니의 다이얼 기억법
# url: https://www.acmicpc.net/problem/5622
# 출처: 나의 네이버 블로그 (blog.naver.com/ydonchoi83)
# 2022.06.19.~2022.07.01.

#########################
# [문제]
# 상근이의 할머니는 아래 그림과 같이 오래된 다이얼 전화기를 사용한다.
# 전화를 걸고 싶은 번호가 있다면, 숫자를 하나를 누른 다음에 금속 핀이 있는 곳 까지 시계방향으로 돌려야 한다.
# 숫자를 하나 누르면 다이얼이 처음 위치로 돌아가고, 다음 숫자를 누르려면 다이얼을 처음 위치에서 다시 돌려야 한다.
# 숫자 1을 걸려면 총 2초가 필요하다.
# 1보다 큰 수를 거는데 걸리는 시간은 이보다 더 걸리며, 한 칸 옆에 있는 숫자를 걸기 위해선 1초씩 더 걸린다.
# 상근이의 할머니는 전화 번호를 각 숫자에 해당하는 문자로 외운다.
# 즉, 어떤 단어를 걸 때, 각 알파벳에 해당하는 숫자를 걸면 된다.
# 예를 들어, UNUCIC는 868242와 같다.
# 할머니가 외운 단어가 주어졌을 때, 이 전화를 걸기 위해서 필요한 최소 시간을 구하는 프로그램을 작성하시오.
# 
# 첫째 줄에 알파벳 대문자로 이루어진 단어가 주어진다. 단어의 길이는 2보다 크거나 같고, 15보다 작거나 같다.
#########################


# be about to revise soon... Below is a prior solution.

def dialword():
    chr = input('할머니가 기억하시는 단어 영문자 입력:').lower()
    dial_chr = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','r','s','t','u','v','w','x','y','z']
    con_num = []
    dial_num = ''
    scnd = 0
    for m in range(1, len(dial_chr)//3+2):
        if m == 1:
            pass
        else:
            for n in range(1,4):
                con_num.append(m)
    for i in range(len(chr)):
        for j in range(len(dial_chr)):
            if chr[i] == dial_chr[j]:
                dial_num += str(con_num[j])
                scnd += int(con_num[j])+1
    print(f"할머니께서 외우고 계신 단어는 {chr} 이며, 해당 다이얼 번호는 {dial_num} 입니다.")
    print(f"전화를 걸기 위해 필요한 최소 시간은 {scnd} 초입니다.")

dialword()


# fin.