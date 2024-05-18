# 49일차: 암호미션5(카이사르암호생성)_1차시도(최영돈(문겸))

print('암호미션5: 카이사르 암호생성')
code=[]
tmp=[]
for i in range(ord('A'), ord('Z')+1):
    code.append(i)
    print(chr(i),end='')
print()
sentence = input('sentence:').upper()
key = int(input('key:'))
for j in range(len(sentence)):
    tmp.append(ord(sentence[j]))
for l in range(len(tmp)):
    for k in range(len(code)):
        if tmp[l] not in range(ord('A'),ord('Z')+1):
            print(chr(tmp[l]),end='')
            break
        elif tmp[l] == code[k]: print(chr(code[(k+key)%26]),end='')