from imagededup.methods import PHash
import os
import sys  # 导入sys模块
from send2trash import send2trash
from os.path import isdir, abspath, getsize, join
from os import listdir, system
from tqdm import tqdm

sys.setrecursionlimit(30000)  # 将默认的递归深度修改为3000

def append_filename(path):
    contents = listdir(abspath(path))
    for content in contents:
        content = join(path, content)
        if isdir(content):
            append_filename(abspath(content))
        else:
            filenames.append(abspath(content))
    return filenames


def del_zero_kb_file(path):
    contents = listdir(abspath(path))
    for content in contents:
        content = join(path, content)
        if isdir(content):
            append_filename(abspath(content))
        else:
            filenames.append(abspath(content))

    for filename in filenames:
        if getsize(filename) == 0:
            system('del %s' % filename)
            print("[-] Deleting %s ..." % filename)


filenames = []
def delete_same():
    phasher = PHash()
    # 需要去重的文件目录
    image_dir = input("请输入图片文件位置： ")
    threshold = int(input("相同图像阈值:"))
    # step1 前置检测 将像素大小为0的文件删掉
    del_zero_kb_file(image_dir)
    # step2 执行查重
    total_encodings = {}

    encodings = phasher.encode_images(image_dir)
    total_encodings.update(encodings)
    duplicates = phasher.find_duplicates(encoding_map=total_encodings,max_distance_threshold=threshold)
    for k, v in tqdm(duplicates.items()):
        if len(v) > 0:
            # step3执行删除
            for file in v:
                file_name_with_full_path = os.path.join(image_dir, file)
                if os.path.exists(file_name_with_full_path):
                    send2trash(file_name_with_full_path)
                    print(file + " del ok")

if __name__ == "__main__":
    delete_same()
