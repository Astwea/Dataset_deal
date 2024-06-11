import cv2
import numpy as np


def show(img):
    cv2.imshow('name', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def resize(img,target_size):
    # 原始图像大小
     

    # 计算原始图像宽高与目标图像大小的比例，并取其中的较小值
    ratio = min(float(target_size[i]) / (old_size[i]) for i in range(len(old_size)))
    # 根据上边求得的比例计算在保持比例前提下得到的图像大小
    new_size = tuple([int(i * ratio) for i in old_size])
    # 根据上边的大小进行放缩
    img = cv2.resize(img, (new_size[1], new_size[0]))
    # 计算需要填充的像素数目（图像的宽这一维度上）
    pad_w = target_size[1] - new_size[1]
    # 计算需要填充的像素数目（图像的高这一维度上）
    pad_h = target_size[0] - new_size[0]
    top, bottom = pad_h // 2, pad_h - (pad_h // 2)
    left, right = pad_w // 2, pad_w - (pad_w // 2)
    img_new = cv2.copyMakeBorder(img, top, bottom, left, right, cv2.BORDER_CONSTANT, None, (0, 0, 0))

    return img_new


def process(img_org):

    kernel = np.ones((3, 3), np.int8)

    img_copy = img_org.copy()
    img_copy_red = img_copy[:,:,2]
    # show(img_copy_red)
    # img_copy_gs = cv2.GaussianBlur(img_copy, (5, 5), 1)
    # show(img_copy)
    _, img_thr = cv2.threshold(img_copy_red, 100, 255, cv2.THRESH_BINARY)
    dst = cv2.adaptiveThreshold(img_copy_red, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 10)
    #show(dst)
    img_new = cv2.morphologyEx(dst, cv2.MORPH_OPEN, kernel, iterations=5)
    edges = cv2.Canny(img_new,100,200)
    contours, h=cv2.findContours(edges,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

    #show(img_new)
    # img_canny = cv2.Canny(img_new, 30, 200)
    # show(img_canny)
    for obj in contours:
        area = cv2.contourArea(obj)  # 计算轮廓内区域的面积
        cv2.drawContours(img_copy, obj, -1, (255, 0, 0), 4)  # 绘制轮廓线
        perimeter = cv2.arcLength(obj, True)  # 计算轮廓周长
        approx = cv2.approxPolyDP(obj, 0.02 * perimeter, True)  # 获取轮廓角点坐标
        CornerNum = len(approx)  # 轮廓角点的数量
        x, y, w, h = cv2.boundingRect(approx)  # 获取坐标值和宽度、高度

        # 轮廓对象分类
        if CornerNum == 3:
            objType = "triangle"
        elif CornerNum == 4:
            if w == h:
                objType = "Square"
            else:
                objType = "Rectangle"
        elif CornerNum > 4:
            objType = "Circle"
        else:
            objType = "N"

        cv2.rectangle(img_copy, (x, y), (x + w, y + h), (0, 0, 255), 2)  # 绘制边界框
        cv2.putText(img_copy, objType, (x + (w // 2), y + (h // 2)), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0, 0, 0),
                    1)  # 绘制文字

    # if circles is not None:
    #     circles = np.uint16(np.around(circles))
    #
    #     # 画出每一个圆
    #     for i in circles[0, :]:
    #         # 绘制外圆
    #         cv2.circle(img_org, (i[0], i[1]), i[2], (0, 255, 0), 2)
    #         # 绘制圆心
    #         cv2.circle(img_org, (i[0], i[1]), 2, (0, 0, 255), 3)
    #         print(i[0], i[1])
        # 显示新图像
        # show(img_org)
    return img_org


if __name__ == '__main__':
    # image_origin = cv2.imread('circle_2.jpg')
    # # image_origin = resize(image_origin,[640,480])
    # show(image_origin)
    # img = process(image_origin)
    # show(img)
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        # frame = cv2.flip(frame, 1)
        image = process(frame)

        cv2.imshow('frame', image)
        # 按q退出视频
        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


