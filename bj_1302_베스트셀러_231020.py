#파이썬 #백준 # #문제풀이 #1302번 #베스트셀러 #최영돈(231028,band.us/@ydonchoi)
'''
(문제)
하루동안 판매된 책의 목록이 출력된다.
판매된 책 중에서 가장 많이 판매된 책의 제목을 출력하는 프로그램을 작성하시오.
첫째 줄에는 판매된 책의 수 N이 주어지고, 다음 줄부터는 책의 제목이 주어진다.
'''
# (해결방안)
# 판매되는 책 중에서 가장 많이 팔린 책의 도서명(key)을 찾는다.

#%%
import operator
N = int(input('금일 판매량:'))
sell = []
print(N)
while len(sell) <= (N-1):
    sell.append(input('판매 도서명:'))
sell2 = list(set(sell))
best_seller = {}
for i in range(len(sell2)):
    cnt = 0
    for j in range(len(sell)):
        if sell2[i]==sell[j]: cnt+=1
    best_seller[sell2[i]] = cnt
print(max(best_seller.items(), key=operator.itemgetter(1)))  # fin.

#%% 모범답안1
def solution_1(N):
    books = []
    for _ in range(N):
        books.append(input('book:'))
    books.sort()
    max_count = 0
    max_book = ""
    for book in books:
        count = books.count(book)
        if count > max_count:
            max_count = count
            max_book = book
    return max_book

def solution_2(N):
    books = {}
    for _ in range(N):
        books.append(input('book:'))
    for book in books:
        books[book] = books.get(book, 0)+1
    max_book = max(books, key = books.get)
    return max_book

T = int(input('test:'))
for _ in range(T):
    N = int(input('sell:'))
    print(solution_1(N))
    print(solution_2(N))
    
# 위의 두 방법 모두 공간 복잡도는 동일하나, 시간복잡도는 1(NlogN), 2(N)이므로 두 번째가 더 효율적임