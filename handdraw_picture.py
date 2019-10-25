from PIL import Image
import numpy as np

a = np.array(Image.open('C:/Users/Administrator/PycharmProjects/untitled/sth interesting/p-1.jpg').convert('L')).astype('float')

depth = 10.
grad = np.gradient(a)    
grad_x, grad_y = grad
grad_x = grad_x*depth/100.
grad_y = grad_y*depth/100.
A = np.sqrt(grad_x**2 + grad_y**2 + 1.)
uni_x = grad_x /A
uni_y = grad_y /A
uni_z = 1. /A

vec_el = np.pi/2.2
vec_az = np.pi/4.
dx = np.cos(vec_el)*np.cos(vec_az)
dy = np.cos(vec_el)*np.sin(vec_az)
dz = np.sin(vec_el)

b = 255*(dx*uni_x + dy*uni_y + dz*uni_z)
b = b.clip(0, 255)

im = Image.fromarray(b.astype('uint8'))
im.save('C:/Users/Administrator/PycharmProjects/untitled/sth interesting/p-1-1.jpg')



'''
这段代码的作用是将一张图片变成手绘的风格,其中一些代码的作用:
7 取图像灰度的梯度值
8 分别取横纵图像梯度值
16 光源的俯视角度，弧度制
17 光源的方位角度，弧度制
18 光源对x轴的影响
19 光源对y轴的影响
20 光源对z轴的影响
22 光源归一化
'''