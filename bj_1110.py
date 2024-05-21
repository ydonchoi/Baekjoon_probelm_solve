# 문제번호: 1110
# 더하기 싸이클
# url: https://www.acmicpc.net/problem/1110
# 23.05.11.

def validation_num(num: int) -> bool:
    return len(str(num)) < 3   # 두 자리 숫자인지 검증

def plus_cycle_str(num: int) -> int:
    tmp, cnt = str(num), 0
    tmp = f'0{tmp[0]}' if len(tmp) < 2 else tmp
    while True:
        a, b = tmp[0],tmp[1]
        cnt +=1
        tmp = str(int(a)+int(b))
        if int(tmp) >= 10: tmp = tmp[1]
        tmp = str(b)+str(tmp)
        if num == int(tmp): break
    return cnt

def plus_cycle_int(num: int) -> int:
    cnt=0
    if num//10 == 0:
        Nnum = num * 10
    Nnum = 10*(num%10) + ((num//10)+(num%10))%10
    while True:
        cnt+=1
        if Nnum == num: break
        else:
            Nnum = 10*(Nnum%10) + ((Nnum//10)+(Nnum%10))%10
    return cnt

def main():
    N = int(input())
    if validation_num(N):
        cnt_str = plus_cycle_str(N)
        cnt_int = plus_cycle_int(N)
        print(f'plus_cycle: {cnt_str}회(sol_str), {cnt_int}회(sol_int)')
    else:
        raise ValueError

if __name__ == '__main__':
    main()

# fin.    