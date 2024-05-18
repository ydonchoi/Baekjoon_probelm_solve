# 37일차: 정수 선택정렬 오름차순_최영돈(문겸)

pList = [95,73,82,83,64,89,77,48,74,99]
print("0차: ", pList)
print("정렬과정")
for k in range(len(pList)):
    tmp=pList[k]
    for i in range(k,len(pList)):
        if pList[i] < tmp: tmp=pList[i]
    pList.remove(tmp)
    pList.insert(k,tmp)
    print(f'{k+1}차:',pList)