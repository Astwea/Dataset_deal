import os
from send2trash import send2trash
path1 = r'../diff'

def file_name(file_dir):
    jpg_list = []
    xml_list = []
    file_dir1 = file_dir + "\\images"
    file_dir2 = file_dir + "\\labels"
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == '.jpg':
                jpg_list.append(os.path.splitext(file)[0])
            elif os.path.splitext(file)[1] == '.txt':
                xml_list.append(os.path.splitext(file)[0])

    diff = set(xml_list).difference(set(jpg_list))  # 差集，在a中但不在b中的元素
    print(len(diff))
    for name in diff:
        print("no jpg", name + ".txt")
        send2trash(file_dir2 + "\\" + name + ".txt")
    diff2 = set(jpg_list).difference(set(xml_list))  # 差集，在b中但不在a中的元素
    print(len(diff2))
    for name in diff2:
        print("no xml", name + ".jpg")
        send2trash(file_dir1 + "\\" + name + ".jpg")
    return jpg_list,xml_list

    # 其中os.path.splitext()函数将路径拆分为文件名+扩展名

def unable_delete():
    path = input("删除无效图片(标签)文件地址:")
    a = input("是否要删除？？？ 1/0")
    if a == '1':
        file_name(path)