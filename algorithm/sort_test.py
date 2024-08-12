import random
from time import time
def my_sort(lst):
    if lst == []:
        return lst
    res = [lst[0]]
    for e in lst[1:]:
        idx = find_insert_idx(res,e)
        res.insert(idx,e)

    return res
def find_insert_idx(res,e):
    for i, elem in enumerate(res):
        if elem > e:
            return i
    return len(res)

def generate_testcases(n):
    testcases = []
    for i in range(n):
        list_length = i + 10000
        testcases.append([random.randint(0,j)
        for j in range(list_length)])
    return testcases

def test_sort(sort_function, testcases):
    data = []
    for case in testcases:
        begin = time()
        len(my_sort(case))
        end = time()

        data.append((len(case), end - begin))
        print((len(case), round(end - begin)))
if __name__ == '__main__':

     begin = time()
     testcases = generate_testcases(10)
     end = time()
     print(end - begin, 2)

     begin = time()
     # test_sort(sorted, testcases)
     test_sort(my_sort, testcases)
     end = time()

     print(f'python sorted tackes {round(end - begin, 2)} second')
     #


