import cv2
import numpy as np

def random_erase(image, p=0.5, s=(0.02, 0.4), r=(0.3, 3)):
    if np.random.rand() > p:
        return image

    img_h, img_w, _ = image.shape

    se = np.random.uniform(s[0], s[1])  # 随机生成挖空区域的面积比例
    re = np.random.uniform(r[0], r[1])  # 随机生成挖空区域的宽高比例

    area = img_h * img_w
    mask_h = int(np.sqrt(se * area * re))
    mask_w = int(np.sqrt(se * area / re))

    top = np.random.randint(0, img_h - mask_h)
    left = np.random.randint(0, img_w - mask_w)
    bottom = top + mask_h
    right = left + mask_w

    image[top:bottom, left:right, :] = 0  # 将挖空区域置为黑色

    return image

# 读取图像
image = cv2.imread('F:\pythonProject\save_img\\342_1.jpg')

# 进行随机挖空数据增强
augmented_image = random_erase(image)

# 显示原始图像和增强后的图像
cv2.imshow('Original Image', image)
cv2.imshow('Augmented Image', augmented_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
