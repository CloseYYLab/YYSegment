import numpy as np
import nibabel as nib
from ipywidgets import interact, interactive, IntSlider, ToggleButtons
import matplotlib.pyplot as plt
import seaborn as sns
import cv2

sns.set_style('darkgrid')


# def explore_3dimage(layer):
#     plt.figure(figsize=(10, 5))
#     plt.imshow(image_data[:, :, layer], cmap='gray');
#     plt.title('Explore Layers of adrenal', fontsize=20)
#     plt.axis('off')
#     return layer


image_path = "D:\segment\Pytorch-Medical-Segmentation-master\Pytorch-Medical-Segmentation-master\logs\your_program_name\step-0100-source.nii.gz"
gt_path = 'D:\segment\Pytorch-Medical-Segmentation-master\Pytorch-Medical-Segmentation-master\logs\your_program_name\step-0100-gt.nii.gz'
pre_path = 'D:\segment\Pytorch-Medical-Segmentation-master\Pytorch-Medical-Segmentation-master\logs\your_program_name\step-0100-predict.nii.gz'

image_obj = nib.load(image_path)
gt_obj = nib.load(gt_path)
pre_obj = nib.load(pre_path)



layer = 111
file_name = ['original_img','gt_img','predict_img']
a = [image_obj.get_fdata(),gt_obj.get_fdata(),pre_obj.get_fdata()]
for index,i in enumerate(a):
    plt.subplot(131+index),plt.imshow(i[:,:,20],cmap='gray'),plt.title(file_name[index]),plt.axis('off')

plt.tight_layout()
plt.show()



# height, width, depth = image_data.shape
# print(f"The image object height: {height}, width:{width}, depth:{depth}")
#
# print(f'image value range: [{image_data.min()}, {image_data.max()}]')
# pixdim = image_obj.header['pixdim']
# print(f'z轴分辨率： {pixdim[3]}')
# print(f'in plane 分辨率： {pixdim[1]} * {pixdim[2]}')
#
# z_range = pixdim[3] * depth
# x_range = pixdim[1] * height
# y_range = pixdim[2] * width
# print(x_range, y_range, z_range)
#
# plt.imshow(image_data)
# plt.axis('off')
# plt.show()
