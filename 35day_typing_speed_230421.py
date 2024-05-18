# 35일차: 타자 측정기(v.0.2) 만들기_최영돈(문겸)

import time as t
print('타자 측정기 v.0.2')
text = ['Now is better than never.', 'Life is too short, you need python.', 'Happy python']
while True:
    start=input('타자측정을 계속하려면 "go"를 입력하세요. 종료하려면 엔터키를 누르세요.:')
    if start == 'go':
        for i in range(len(text)):
            textlngth=0
            totaltime=0
            while True:
                stime=0
                etime=0
                stime=t.time()
                print(f'제시 문장:{text[i]}')
                typing = str(input('>'))
                if typing != text[i]:
                    print('오타가 있습니다.')
                else:
                    etime=t.time()
                    dtime=etime-stime
                    textlngth+=len(text[i])
                    totaltime+=dtime
                    speed=(len(text[i])/dtime)*60
                    print(f'{round(speed)}타/분')
                    break
        print(f'전체 타수: {round((textlngth/totaltime)*60)}타/분')
    else:
        print('탈출! yeap!')
        break
