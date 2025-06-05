# Dataset_deal

`Dataset_deal` 提供了一组处理图像数据集的脚本，可用于数据增强、
数据集划分、图片批量操作等任务。脚本大多通过命令行交互的方式
运行，适合在小规模数据集上快速实验。

## 依赖

项目基于 Python 3 开发，运行脚本前需要安装以下第三方包：

```
opencv-python
numpy
Pillow
tqdm
send2trash
imagededup
```

可使用 `pip install 包名` 安装，或根据实际情况创建 `requirements.txt`
后批量安装。

## 快速开始

1. 克隆仓库后进入目录：
   ```bash
   git clone https://github.com/Astwea/Dataset_deal.git
   cd Dataset_deal
   ```
2. 安装依赖。
3. 运行主脚本并按提示选择需要的功能：
   ```bash
   python main.py
   ```

主脚本包含如下功能编号：

1. 计算标签类别数量
2. 根据类别删除标签文件
3. 根据图片内容删除数据
4. 删除重复图片
5. 删除无效图片或标签
6. 图像数据增强
7. 划分训练/测试集
8. 批量重命名图片
9. 按比例分组图片
10. 批量调整图片尺寸

根据提示输入对应编号即可执行相应操作。

## 目录说明

- `main.py`：命令行入口，整合各类功能。
- `data_strong.py`：封装的图像增强流程。
- `utils/`：具体功能脚本，如图片去重、分割、重命名等。

仓库中的脚本大多采用交互式方式获取路径和参数，运行过程中请
根据提示输入相应信息。

