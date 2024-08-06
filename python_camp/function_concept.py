import math
# --------------------------------------------
# 1. 함수의 다양한 입력들 살펴보기 
#
# 1) input이 없는 함수 
# 2) input이 여러 개 있는 함수 
# 3) input이 정해지지 않은 갯수만큼 있는 함수 
# --------------------------------------------

def pi():
    """원주율을 소숫점 두 자리까지 반환하는 함수
    """
    return  round(math.pi, 2)
print(pi())
def left_append(lst, elem):
    """lst의 왼쪽에 elem을 넣고, lst를 반환하는 함수
    """
    lst.insert(0, elem)
    return lst
lst = [1, 2, 3, 4]
result = left_append(lst, 0)
print(result)
def left_extend(lst, *elems):
    """lst의 왼쪽에 정해지지 않은 개수의 elems을 넣고 lst를 반환하는 함수
    """
    return list(elems) + lst
lst = [1, 2, 3, 4]
result = left_extend(lst, 0,6,9,7)
print(result)
# --------------------------------------------
# 2. 함수의 call stack 알아보기 
# 
# 1) 아래 함수 b()를 실행할 때, 실행된 함수의 순서는?
# --------------------------------------------
def a():
    return pi()

def b():
    return a()
#############   답  :  위에 pi 함수 실행
# --------------------------------------------
# 2) 아래 함수 c()를 실행할 때, 실행된 함수의 순서와 각 함수의 input은? 
# --------------------------------------------
def c(lst):
    if not lst:
        return print('끝')
    print(lst[0])
    return c(lst[1:])
c(list(range(10)))
#############   답  :
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# error(빈 리스트에서 값을 가져오려해서 Index Error가 남)