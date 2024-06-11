import os
from send2trash import send2trash
from tqdm import tqdm
def delete_labels_with_class():
    label_folder = input("labels文件地址:")
    class_id = input("需删除的ID:")
    num = int(input("删除数量:"))
    x = 0
    pbar = tqdm(total=num)
    for filename in os.listdir(label_folder):
        label_file = os.path.join(label_folder, filename)

        with open(label_file, 'r') as file:
            lines = file.readlines()

        contains_class = False

        for line in lines:
            label = line.strip().split(' ')  # 使用空格分隔每行的元素
            current_class_id = label[0]  # 假设每行的第一个元素是类别ID

            if current_class_id == class_id:
                contains_class = True
                x = x + 1
                pbar.update(1)
                break
        if x == num:
            return
        if contains_class:
            send2trash(label_file)