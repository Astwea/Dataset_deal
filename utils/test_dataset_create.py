import os
import cv2
import numpy as np
import shutil
from tqdm import tqdm

def test_create():
    image_path = input("照片位置:")
    label_path = input("标签位置：")
    create_root = input("数据集建立位置:")
    test_num = int(input("测试集数量"))  #测试集数量
    image_dir = os.path.join(image_path)
    label_dir = os.path.join(label_path)
    image_names = os.listdir(image_dir)
    label_names = os.listdir(label_dir)
    os.makedirs(create_root + "/train/images/")
    os.makedirs(create_root + "/test/images/")
    os.makedirs(create_root + "/train/labels/")
    os.makedirs(create_root + "/test/labels/")
    path1 = create_root + "/train\images\\"
    path2 = create_root + "/test\images\\"
    path3 = create_root + "/train\labels\\"
    path4 = create_root + "/test\labels\\"
    num = []
    for i in tqdm(range(test_num)):
        ls = np.random.randint(0, len(image_names))
        if ls not in num:
            num.append(ls)
            img_dir = os.path.join(image_dir, image_names[ls])
            lab_dir = os.path.join(label_dir, label_names[ls])
            shutil.copy(lab_dir, path4+label_names[ls])
            img = cv2.imread(img_dir)
            cv2.imwrite(path2+image_names[ls], img)
    for a in tqdm(range(len(image_names))):
        if a in num:
            continue
        img_dir = os.path.join(image_dir, image_names[a])
        lab_dir = os.path.join(label_dir, label_names[a])
        shutil.copyfile(lab_dir, path3 + label_names[a])
        img = cv2.imread(img_dir)
        cv2.imwrite(path1 + image_names[a], img)
