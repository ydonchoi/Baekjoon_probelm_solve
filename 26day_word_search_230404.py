# 26일차: 영어 단어 검색하기1_최영돈(문겸)
print('Eng_word search v0.1')
def enroll_word(myDic: dict, word: str) -> dict:
    meaning = input(f'enter the meaning of the {word}:')
    myDic[word] = meaning
    return myDic

def main():
    myDic = {}
    test = int(input('testing number:'))
    for _ in range(test):
        word = input('enter a word:')
        if word in myDic.keys():
            print(f'The {word} means {myDic[word]}.')
        else:
            print('there is not in my dic.')
            yn = input(f'Do you want to enroll the {word}? (y/n):').lower()
            if yn[0] == 'y':
                myDic = enroll_word(myDic, word)

if __name__ == "__main__":
    main()