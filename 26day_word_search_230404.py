# 26일차: 영어 단어 검색하기1_최영돈(문겸)
print('영어 단어검색 v.0.1')
while True:
    myDic={'sky':'하늘','apple':'사과','can':'깡통','boat':'배','sea':'바다','smile':'미소','animal':'동물','park':'공원'}
    search=[]
    word=input('단어입력:')
    if word == '':
        print('탈출! yeap!')
        break
    else:
        for key in myDic.keys():
            if word == key:
                search.append(word)
                print(f'{word}의 뜻은 {myDic[word]}입니다.')
                pass
            else: pass
        if search == []:
            print(f'{word} 단어는 단어장에 없음')
