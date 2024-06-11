import os
import cv2
from send2trash import send2trash

path1 = r'../diff'

def delete_choose():
    file_dir = input("需要选择删除的数据集(train/test)地址(d:删除，s:保存，q:退出):")
    file_dir1 = file_dir+"\\images"
    file_dir2 = file_dir+"\\labels"
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            print(file_dir1+"\\"+file)
            img = cv2.imread(file_dir1+"\\"+file)
            cv2.imshow("choose", img)
            a = cv2.waitKey(0)
            if a == ord('d'):
                try:
                    send2trash(file_dir2 + "\\" + os.path.splitext(file)[0] + ".txt")
                    print("删除成功")
                    cv2.destroyAllWindows()
                except:
                    print("删除失败")
                    cv2.destroyAllWindows()
            if a == ord('s'):
                cv2.destroyAllWindows()
            if a == ord('q'):
                cv2.destroyAllWindows()

if __name__ == '__main__':
    delete_choose()