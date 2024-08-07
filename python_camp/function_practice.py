import os.path
import random

# --------------------------------------------
# 1. max / min 구현하기 
#
# cmp라는 함수를 이용한 min/max 구현하기. 
# cmp는 두 원소 중 더 큰 것을 반환하는 함수. 
# --------------------------------------------
def my_max(lst, cmp=lambda x, y: x):
    result = lst[0]
    for item in lst[1:]:
        result = cmp(result, item)
    return result

max_list = [10,5,9,4,2,3,4,5,6,7,4,2,2,3,4,11,6]
print('최댓값 : ', my_max(max_list, cmp=lambda x, y: x if x > y else y))

def my_min(lst, cmp=lambda x, y: x):
    result = lst[0]
    for item in lst[1:]:
        result = cmp(result, item)
    return result

min_list = [10,5,9,4,2,3,4,5,6,7,4,2,2,3,4,1,6]
print('최솟값 : ', my_min(min_list, cmp=lambda x, y: x if x < y else y))

# --------------------------------------------
# 2. sort 구현하기 
# 
# 1) 그냥 순서대로 오름차순으로 정렬하기 
# 2) 오름차순, 내림차순으로 정렬하기 
# 3) 주어진 기준 cmp에 맞춰서 오름차순, 내림차순으로 정렬하기 
# 4) 주어진 기준 cmp가 큰 element를 출력하거나, 같다는 결과를 출력하게 만들기 
# 5) cmp상 같은 경우 tie-breaking하는 함수 넣기 
# --------------------------------------------
print()
print('**************************************************************')
print()
def sort1(lst):

    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst
sort_lst = [2, 7, 4, 1, 5, 6, 8, 2, 3, 5, 4]
print(f'오름차순: {sort1(sort_lst)}')


print()
print('**************************************************************')
print()
def sort2(lst, upper_to_lower=True):
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if upper_to_lower:
                if lst[j] > lst[j + 1]:
                    lst[j], lst[j + 1] = lst[j + 1], lst[j]
            else:
                if lst[j] < lst[j + 1]:
                    lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

sort_lst = [2, 7, 4, 1, 5, 6, 8, 2, 3, 5, 4]
print(f'오름차순: {sort2(sort_lst, upper_to_lower=True)}')
print()
print(f'내림차순: {sort2(sort_lst, upper_to_lower=False)}')


print()
print('**************************************************************')
print()
def sort3(lst, upper_to_lower=True, cmp=lambda x, y: x):
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if upper_to_lower:
                if cmp(lst[j + 1], lst[j]):
                    lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

sort_lst = [2, 7, 4, 1, 5, 6, 8, 2, 3, 5, 4]
print(f'오름차순: {sort3(sort_lst, upper_to_lower=True, cmp=lambda x, y: x < y)}')
print()
print(f'내림차순: {sort3(sort_lst, upper_to_lower=True, cmp=lambda x, y: x > y)}')



def sort4(lst, upper_to_lower = True, cmp = lambda x, y: x):
    ...

print()
print('**************************************************************')
print()


import random

def sort5(lst, upper_to_lower=True, cmp=lambda x, y: x, tie_breaker=lambda x, y: random.choice([x, y])):
    n = len(lst)

    def demo_sort5(x, y):
        if cmp(x, y):
            return True
        elif cmp(y, x):
            return False
        else:
            return tie_breaker(x, y) == x

    for i in range(n):
        for j in range(0, n - i - 1):
            if upper_to_lower:
                if demo_sort5(lst[j], lst[j + 1]):
                    lst[j], lst[j + 1] = lst[j + 1], lst[j]
            else:
                if demo_sort5(lst[j + 1], lst[j]):
                    lst[j], lst[j + 1] = lst[j + 1], lst[j]

    return lst
sort_lst = [(1, 4), (1, 5), (1, 2), (40, 24), (3, 1), (5, 4), (1, 3),(3,3)]
sort_lst_desc = sort5(
    sort_lst.copy(),
    upper_to_lower=True,
    cmp=lambda x, y: (x[0] > y[0]) or (x[0] == y[0] and x[1] > y[1]),
    tie_breaker=lambda x, y: random.choice([x, y])
)
print(f'내림차순: {sort_lst_desc}')
sort_lst_asc = sort5(
    sort_lst.copy(),
    upper_to_lower=True,
    cmp=lambda x, y: (x[0] < y[0]) or (x[0] == y[0] and x[1] < y[1]),
    tie_breaker=lambda x, y: random.choice([x, y])
)
print(f'오름차순: {sort_lst_asc}')





# --------------------------------------------
# os_file_concept.py 해보고 올 것 
# --------------------------------------------

# --------------------------------------------
# 3. safe pickle load/dump 만들기 
# 
# 일반적으로 pickle.load를 하면 무조건 파일을 읽어와야 하고, dump는 써야하는데 반대로 하면 굉장히 피곤해진다. 
# 이런 부분에서 pickle.load와 pickle.dump를 대체하는 함수 safe_load, safe_dump를 짜 볼 것.  
# hint. 말만 어렵고 문제 자체는 정말 쉬운 함수임.
# --------------------------------------------

def safe_load(pickle_path):
    pass 

def safe_dump(pickle_path):
    pass 


# --------------------------------------------
# 4. 합성함수 (추후 decorator)
# 
# 1) 만약 result.txt 파일이 없다면, 함수의 리턴값을 result.txt 파일에 출력하고, 만약 있다면 파일 내용을 읽어서 
#    '함수를 실행하지 않고' 리턴하게 하는 함수 cache_to_txt를 만들 것. txt 파일은 pickle_cache 폴더 밑에 만들 것.  
# 2) 함수의 실행값을 input에 따라 pickle에 저장하고, 있다면 pickle.load를 통해 읽어오고 없다면 
#    실행 후 pickle.dump를 통해 저장하게 하는 함수 cache_to_pickle을 만들 것. pickle 파일은 pickle_cache 폴더 밑에 만들 것. 
# 3) 함수의 실행값을 함수의 이름과 input에 따라 pickle에 저장하고, 2)와 비슷하게 진행할 것. pickle 파일은 pickle_cache 폴더 밑에, 각 함수의 이름을 따서 만들 것 
# --------------------------------------------

def cache_to_txt(function):
    pass 

def cache_to_pickle(function):
    ...

