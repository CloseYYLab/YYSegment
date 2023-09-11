import torchio as tio
import matplotlib.pyplot as plt

image_path = 'D:\segment\labelled\labelled\image\Teeth_0001_0000.nii.gz'
subject = tio.Subject(
    image=tio.ScalarImage(image_path),
)

# 定义 CropOrPad 变换
crop_or_pad = tio.CropOrPad(target_shape=(288, 288, 224), padding_mode='reflect')
crop_or_pad1 = tio.CropOrPad(target_shape=(266, 266, 200), padding_mode='reflect')

# 对图像应用变换
transformed_subject = crop_or_pad(subject)
transformed_subject1 = crop_or_pad1(transformed_subject)
# 获取变换后的图像
transformed_image = transformed_subject.image.data.squeeze().numpy()

transformed_image1 = transformed_subject1.image.data.squeeze().numpy()

# 展示原始图像和变换后的图像
plt.subplot(131), plt.imshow(subject.image.data.squeeze().numpy()[:, :, 64], cmap='gray'), plt.title('original_img')
plt.subplot(132), plt.imshow(transformed_image[:, :, 64], cmap='gray'), plt.title('change_img')
plt.subplot(133), plt.imshow(transformed_image1[:, :, 64], cmap='gray'), plt.title('changechange_img')
plt.tight_layout()
plt.show()
