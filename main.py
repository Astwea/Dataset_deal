from To_dataset.utils.count import count_labels
from To_dataset.utils.delete_class_label import delete_labels_with_class
from To_dataset.utils.delete_dataset import delete_choose
from To_dataset.utils.delete_same_dataset import delete_same
from To_dataset.utils.delete_unable_dataset import unable_delete
from data_strong import data_stronger
from To_dataset.utils.rename_image import rename
from To_dataset.utils.test_dataset_create import test_create
from To_dataset.utils.resize_image import resize_
from To_dataset.utils.split_image import spilt_image


if __name__ == "__main__":
    while 1:
        key = input("选择功能:\n 【1】计算标签种类数量\t 【2】删除种类标签\n 【3】根据图片删除数据\t"
                    " 【4】删除相似照片\n 【5】删除无效的图片(标签) \t 【6】数据增强 \n 【7】数据集生成 \t"
                    " 【8】批量命名 \n 【9】图片分组\t 【10】批量resize\n 【q】退出 \n :")
        if key == '1':
            count_labels()
        elif key == '2':
            delete_labels_with_class()
        elif key == '3':
            delete_choose()
        elif key == '4':
            delete_same()
        elif key == '5':
            unable_delete()
        elif key == '6':
            data_stronger()
        elif key == '7':
            test_create()
        elif key == '8':
            rename()
        elif key == '9':
            spilt_image()
        elif key == '10':
            resize_()
        elif key == 'q':
            break
        else:
            print("请输入正确数字")