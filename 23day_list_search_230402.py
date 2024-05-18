# %%
# 23일차: 리스트 검색하기3 _ (최영돈(문겸))
# code revision_updated(24.04.26)

wordList = ['cat','dog','pig','hen','cow','duck','cat']
while word := input("단어 입력:").lower():
    if word == "":
        break
    print(f'입력 단어:{word}')
    word_location = [i for i, w in enumerate(wordList) if word == w]    
    if word_location == []:
        print(f"{word}는 검색할 수 없음.")
        yn=input("추가할까요?(y/n)").lower()
        if yn == "y":
            wordList.append(word)
            print(f'{word} 추가됨')
    else:
        print(f"{word}는 {word_location}번째에 있다.")


