import cv2
import os
from tqdm import tqdm

def spilt_image():
    image_path = input("文件地址:")
    name = input("文件夹命名为: ")
    n = int(input("需要分成几份："))
    image_dir = os.path.join(image_path)
    image_names = os.listdir(image_dir)
    c = int(len(image_names)/n)
    for i in range(n):
        os.makedirs(f"{name}{i}")
    i = 0
    d = c
    for j in tqdm(range(len(image_names))):
        if j > c:

            i += 1
            c += d
        img_dir = os.path.join(image_dir, image_names[j])
        img = cv2.imread(img_dir)
        cv2.imwrite(f"{name}{i}//"+image_names[j], img)

if __name__ == "__main__":
    spilt_image()