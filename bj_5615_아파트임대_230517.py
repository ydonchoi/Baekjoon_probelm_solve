#코딩 #파이썬 #백준 #문제풀이 #5615번(아파트임대문제)

a=list(map(int,input('면적 입력:').split(',')))
judge,sol,cnt=[],{},0
for k in a:
    for x in range(1,k):
        for y in range(1,k):
            if k==(2*x*y)+x+y:
                sol.update({k:(x,y)})
                judge.append(True)
    if len(judge) >= 1 : judge = []
    else: cnt+=1
print(f'없는 면적의 수: {cnt}\n면적별 x, y의 값: {sol}')