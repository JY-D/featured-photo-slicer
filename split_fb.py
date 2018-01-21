import cv2
import numpy as np 

img = cv2.imread('your_photo_name.jpg')
height = np.shape(img)[0]
x_y = np.shape(img)[1] - np.shape(img)[0]
#x_start don't > x_y
x_start = 0

split_img1 = img[:int(height/2), x_start:int(x_start+(height/2)), :]
split_img2 = img[int(height/2):, x_start:int(x_start+(height/2)), :]
split_img3 = img[:int(height/3), int(x_start+(height/2)):-(x_y - x_start), :]
split_img4 = img[int(height/3):int(2 * height/3), int(x_start+(height/2)):-(x_y - x_start), :]
split_img5 = img[int(2 * height/3): , int(x_start+(height/2)):-(x_y - x_start), :]

cv2.imwrite('./split/split_img1.png',split_img1)
cv2.imwrite('./split/split_img2.png',split_img2)
cv2.imwrite('./split/split_img3.png',split_img3)
cv2.imwrite('./split/split_img4.png',split_img4)
cv2.imwrite('./split/split_img5.png',split_img5)