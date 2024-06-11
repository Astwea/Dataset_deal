import os

def count_labels():
    label_folder = input("标签地址:")
    label_counts = {}

    for file_name in os.listdir(label_folder):
        label_file = os.path.join(label_folder, file_name)
        with open(label_file, 'r') as file:
            lines = file.readlines()

        for line in lines:
            labels = line.strip().split()[0:]  # 假设每行标签以空格分隔，并且第一个元素是图像文件名
            for label in labels:
                class_id = label.split(' ')[0]  # 假设类别ID在标签中的第一个元素，并且以逗号分隔
                if class_id in label_counts:
                    label_counts[class_id] += 1
                    break
                else:
                    label_counts[class_id] = 1
                    break
    print(label_counts)

# 调用示例
if __name__ == "__main__":
    count_labels()
