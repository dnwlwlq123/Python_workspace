import os
import shutil
# --------------------------------------------
# 1. os 활용 예제 
# 
# 1) os 디렉토리 구조 출력해보기 
# 2) root directory 아래에 있는 특정 확정자 파일들 다 출력하기 
# 3) os 디렉토리 복사하기 
# --------------------------------------------
route = 'C:\\Users\\user\\Desktop'



print("***************************************************")
def print_directory_tree(root):
    global route

    def recursive_list(current, deep=0):
        root_item = os.listdir(current)
        if deep == 3:
            return
        for elem in root_item:
            full_path = os.path.join(current, elem)
            if os.path.isdir(full_path):
                print(f"{'  ' * deep}<DIR>\t\t\t{elem}")
                recursive_list(full_path, deep + 1)
            else:
                print(f"{'  ' * deep}file\t\t\t{elem}")
    recursive_list(root)
print_directory_tree(route)

print("***************************************************")
def list_extension_files(root):
    global route

    for elem in os.listdir(root):
        full_path = os.path.join(root, elem)
        if not os.path.isdir(full_path):
            name_extension = os.path.splitext(elem)
            extension = name_extension[1]
            if extension:
                extension = extension[1:]
                if extension == 'txt':
                    print(f'{extension} 파일입니다 \t {elem}' )
                elif extension == 'pdf':
                    print(f'{extension} 파일입니다 \t{elem}')
                elif extension == 'py':
                    print(f'{extension} 파일입니다 \t {elem}' )
                elif extension == 'ini':
                    print(f'{extension} 파일입니다 \t{elem}')
list_extension_files(route)
print()
print("***************************************************")
def copy_directory(origin_dir, copy_dir):

    if not os.path.exists(copy_dir):
        os.makedirs(copy_dir)
    for elem in os.listdir(origin_dir):
        full_path = os.path.join(origin_dir, elem)
        copy_path = os.path.join(copy_dir, elem)
        if os.path.isdir(full_path):
            copy_directory(full_path, copy_path)
        else:
            parent_dir = os.path.dirname(copy_path)
            if not os.path.exists(parent_dir) :
                os.makedirs(parent_dir)
            elif not os.path.exists(copy_path) :
                shutil.copy2(full_path, copy_path)
                os.path.isdir(full_path)
                print(f'\t{elem}\t\t**복사완료**')
            else :
                print("디렉토리가 이미 존재함")

copy_directory('C:\\Users\\user\\Desktop\\dir_practice', 'C:\\Users\\user\\Desktop\\copy_test')

    