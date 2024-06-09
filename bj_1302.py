# 문제번호: 1302
# 베스트셀러
# url: https://www.acmicpc.net/problem/1302
# 23.10.28.

##############################################
# (문제)
# 하루동안 판매된 책의 목록이 출력된다.
# 판매된 책 중에서 가장 많이 판매된 책의 제목을 출력하는 프로그램을 작성하시오.
# 첫째 줄에는 판매된 책의 수 N이 주어지고, 다음 줄부터는 책의 제목이 주어진다.
##############################################

# ''''''''''''''''''
# # (해결방안)
# # 판매되는 책 중에서 가장 많이 팔린 책의 도서명(key)을 찾는다.
# ''''''''''''''''''

# My_Solution
def gen_sell_quantity(quantity: int) -> list:
    return [input('판매 도서명:') for _ in range(quantity)]

def check_unique_book_list(sell_list: list) -> list:
    return list(set(sell_list))

def check_best_seller(sell_list: list, unique_book_list: list) -> dict:
    best_seller = {}
    for ind_book in unique_book_list:
        cnt = sum(1 for book in sell_list if ind_book == book)
        best_seller[ind_book] = cnt
    return best_seller

def main():
    quantity = int(input('금일 판매량:'))
    sell_list = gen_sell_quantity(quantity)
    unique_book_list = check_unique_book_list(sell_list)
    best_seller = check_best_seller(sell_list, unique_book_list)
    print(max(best_seller.items(), key=operator.itemgetter(1)))

if __name__ == '__main__':
    import operator
    main()    


# fin.



#%% 모범답안
# def solution_1(N):
#     books = []
#     for _ in range(N):
#         books.append(input('book:'))
#     books.sort()
#     max_count = 0
#     max_book = ""
#     for book in books:
#         count = books.count(book)
#         if count > max_count:
#             max_count = count
#             max_book = book
#     return max_book

# def solution_2(N):
#     books = {}
#     for _ in range(N):
#         books.append(input('book:'))
#     for book in books:
#         books[book] = books.get(book, 0)+1
#     max_book = max(books, key = books.get)
#     return max_book

# T = int(input('test:'))
# for _ in range(T):
#     N = int(input('sell:'))
#     print(solution_1(N))
#     print(solution_2(N))
    
# # 위의 두 방법 모두 공간 복잡도는 동일하나, 시간복잡도는 1(NlogN), 2(N)이므로 두 번째가 더 효율적임
