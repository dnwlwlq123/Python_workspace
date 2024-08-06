import os 
import pickle
import shutil
from time import time
# --------------------------------------------
# 1. os 기초 예제 
# 
# 1) os.path 이해하기 (os.path.exists, os.path.join, os.path)
# 2) os.listdir / os.makedir 해보기 
# 3) os.getcwd / os.changedir 해보기 
# --------------------------------------------

# print(os.getcwd())
#
# # for elem in os.listdir('C:\\Users\\user\\Desktop\\python\\python_camp'):#절대경로 쓰는건 안좋은 방법
# for elem in os.listdir():
#     if os.path.isdir(elem):
#         print(f'<DIR>\t\t{elem}')
#     elif '.' in elem:
#         extension = elem.split('.')[-1]
#         print(f'{extension} file\t' + elem)
#
# def create_dir(directory_name):
#     if not os.path.exists(directory_name):
#         print(f'{directory_name} does not exists')
#         os.makedirs(directory_name)
#     else :
#         print(f'{directory_name} does exists')
# create_dir('hello world')


#상대경로 = 현재 내가 있는 디렉토리에서의 경로
#절대경로 = C: 에서 부터 일컫는 경로
# def delete_dir(directory_del):
#     if os.path.exists(directory_del):
#         shutil.rmtree(directory_del)
#         print(f'{directory_del} 디렉토리가 성공적으로 삭제되었습니다.')
#     else:
#         print(f'{directory_del}는 존재하지 않는 디렉토리입니다.')
#
#
# delete_dir('hello world')

# --------------------------------------------
# 2. file 기초 예제
# 1) open 이해하기 
# 2) 파일 읽기, 써보기 
# --------------------------------------------

# 여는걸로 시작 닫는걸로 끝 w+ 기존에 있던걸 다 날림, a+ 기존에 있던걸 보존
# f = open('example.txt', 'a+', encoding = 'utf-8')
# h = 'hello python'
# k = 'kim tae jin'
# for i in range(101):
#     # print(i, file = f)
#     # f.write(str(i) + '\n')
#     print(h, '\n'+k, file = f)
# f.close()
######################################################

# begin = time()
# f = open('example.txt', 'w+', encoding = 'utf-8')
# for i in range(10):
#     print(str(i)*10, file = f)
# f.close()
# end = time()
# print(f'{end - begin}sec passed for making example.txt')

######################################################
# begin = time()
# f = open('example.txt', 'r', encoding = 'utf-8')
# print(f.readline())
# for line in f.readlines():
#     print(line)
# f.close()
# end = time()
# print(f'{end - begin}sec passed for making example.txt')
# --------------------------------------------
# 3. pickle 기초 예제 
# pickle => check 포인트 (중간 학습 결과를 보고싶을때)
# 1) pickle.load() 해보기 
# 2) pickle.dump() 해보기 
# --------------------------------------------
#wb=> bite로 저장하겠다
# d = {'name':'kim tae jin'}
#
# pickle.dump(d,open('empty_dict.pickle', 'wb+'))
# e = pickle.load(open('empty_dict.pickle', 'rb'))
# print(e)