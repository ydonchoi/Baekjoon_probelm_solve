# 33일차: 타자 측정기(v.0.1) 만들기_최영돈(문겸)

import time as t
print('타자 측정기 v.0.1')
sentence = '동해물과 백두산이 마르고 닳도록 하느님이 보우하사 우리나라 만세. 무궁화 삼천리 화려강산 대한사람 대한으로 길이 보전하세.'
print(f'제시 문장:{sentence}')
while True:
    stime=t.time()
    typing = str(input('>'))
    if typing == '':
        print('탈출! yeap!')
        break
    else:
        if typing != sentence:
            print('오타가 있습니다.')
        else:
            etime=t.time()
            dtime=(len(sentence)/round(etime-stime))*60
            print(f'{int(dtime)}타/분')