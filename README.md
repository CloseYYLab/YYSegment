# Pytorch Medical Segmentation
<i>英文版请戳：<a href='https://github.com/MontaEllis/Pytorch-Medical-Segmentation/blob/master/README.md'>这里！</a></i><br />


## 环境要求
* pytorch1.7
* torchio<=0.18.20
* python>=3.6

## 通知
* 您可以修改**hparam.py**文件来确定是2D分割还是3D分割以及是否可以进行多分类。
* 我们几乎提供了所有的2D和3D分割的算法。
* 本项目兼容几乎所有的医学数据格式(例如 nii.gz, nii, mhd, nrrd, ...)，修改**hparam.py**的**fold_arch**即可。**我希望您能在使用前把source和label图片都转成相同的类型，其中，label用1标志，不是255。**
* 如果您想进行**多分类**分割，请自行修改对应代码。我不能确定您的具体分类数。
* 不论是2D或是3D，本项目均采用**patch**的方式。故图片大小不必严格保持一致。在2D中，您应该把patch设置的足够大。

## 准备您的数据
### 例1
如果您的source文件夹如下排列 :
```
source_dataset
├── source_1.mhd
├── source_1.zraw
├── source_2.mhd
├── source_2.zraw
├── source_3.mhd
├── source_3.zraw
├── source_4.mhd
├── source_4.zraw
└── ...
```

同时您的label文件夹如下排列 :
```
label_dataset
├── label_1.mhd
├── label_1.zraw
├── label_2.mhd
├── label_2.zraw
├── label_3.mhd
├── label_3.zraw
├── label_4.mhd
├── label_4.zraw
└── ...
```

您应该修改 **fold_arch** 为 **\*.mhd**, **source_train_dir** 为 **source_dataset** 并修改 **label_train_dir** 为 **label_dataset** in **hparam.py**

### Example2
如果您的source文件夹如下排列 :
```
source_dataset
├── 1
    ├── source_1.mhd
    ├── source_1.zraw
├── 2
    ├── source_2.mhd
    ├── source_2.zraw
├── 3
    ├── source_3.mhd
    ├── source_3.zraw
├── 4
    ├── source_4.mhd
    ├── source_4.zraw
└── ...
```

同时您的label文件夹如下排列 :
```
label_dataset
├── 1
    ├── label_1.mhd
    ├── label_1.zraw
├── 2
    ├── label_2.mhd
    ├── label_2.zraw
├── 3
    ├── label_3.mhd
    ├── label_3.zraw
├── 4
    ├── label_4.mhd
    ├── label_4.zraw
└── ...
```

您应该修改 **fold_arch** 为 **\*/\*.mhd**, **source_train_dir** 为 **source_dataset** 并修改 **label_train_dir** 为 **label_dataset** in **hparam.py**


## 训练
* 不使用预训练模型
```
set hparam.train_or_test to 'train'
python main.py
```
* 使用预训练模型
```
set hparam.train_or_test to 'train'
python main.py -k True
```
  
## Inference
* 测试
```
set hparam.train_or_test to 'test'
python main.py
```

## 实例
![](https://ellis.oss-cn-beijing.aliyuncs.com/img/20210108185333.png)
![](https://ellis.oss-cn-beijing.aliyuncs.com/img/2021-02-06%2022-40-07%20%E7%9A%84%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE.png)


## 教程
* https://www.bilibili.com/video/BV1gp4y1H7kq/


## Done
### Network
* 2D
- [x] unet
- [x] unet++
- [x] miniseg
- [x] segnet
- [x] pspnet
- [x] highresnet(copy from https://github.com/fepegar/highresnet, Thank you to [fepegar](https://github.com/fepegar) for your generosity!)
- [x] deeplab
- [x] fcn
* 3D
- [x] unet3d
- [x] residual-unet3d
- [x] densevoxelnet3d
- [x] fcn3d
- [x] vnet3d
- [x] highresnert(copy from https://github.com/fepegar/highresnet, Thank you to [fepegar](https://github.com/fepegar) for your generosity!)
- [x] densenet3d
- [x] unetr (copy from https://github.com/tamasino52/UNETR)

### Metric
- [x] metrics.py 来评估您的结果

## TODO
- [ ] dataset
- [ ] benchmark
- [ ] nnunet


## 致谢
这个项目是一个非官方PyTorch实现的3D和2D医学分割，高度依赖于[MedicalZooPytorch](https://github.com/black0017/MedicalZooPytorch)和[torchio](https://github.com/fepegar/torchio)。感谢上述项目。本项目在[Prof. Ruoxiu Xiao](http://enscce.ustb.edu.cn/Teach/TeacherList/2020-10-16/114.html) 和 [Dr. Cheng Chen](b20170310@xs.ustb.edu.cn)的指导下完成。感谢[Youming Zhang](zhangym0820@csu.edu.cn), [Daiheng Gao](https://github.com/tomguluson92), [Jie Zhang](jpeter.zhang@connect.polyu.hk), [Xing Tao](kakatao@foxmail.com), [Weili Jiang](1379252229@qq.com)和[Shanshan Li](https://github.com/ssli23) 对我的帮助。

