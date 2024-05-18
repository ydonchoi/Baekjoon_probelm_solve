#문제풀이 #백준 #1463번_분해합 #24.02.27

def rslvsum(num:int) -> int:
    cnt = 0
    while num > 1:
        if num % 3 == 1:
            cnt += 1
            num -= 1
        if num % 3 == 0:
            cnt += 1
            num //= 3
        if num % 2 == 0:
            cnt += 1
            num //= 2
    return cnt

cnt = rslvsum(10)
print(cnt)     # fin.
