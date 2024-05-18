# 36일차: 리스트 짝지어 정렬하기_최영돈(문겸)

nameList=['김','이','박','최','정','강','조','윤','장','임']
pList=[95,73,82,83,64,89,77,48,74,99]
rslt={}
for i in range(len(nameList)): rslt.update({nameList[i]:pList[i]})
 # 또는 for i, j in zip(nameList,pList): rslt.update({i:j})
for j in sorted(rslt): print(j,rslt[j])