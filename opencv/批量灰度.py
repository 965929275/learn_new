# -*- coding:utf-8 -*-
import cv2
# 注意路径
j = 1
while j < 5:
    input_img = cv2.imread('aaa/'+ str(j) + '.jpg')
    utput_image = cv2.cvtColor(input_img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('bbb/%d.jpg' % j, utput_image)
    j += 1