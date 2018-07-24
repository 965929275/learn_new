## 目的：利用Opencv检测图片中的钢筋个数

### 1. 首先进行图片的预处理

1. 进行**前景检测**然后对提取出的像素（成捆的钢筋）做下一步的操作，网上找了一些算法，如下：

   ```python
   import numpy as np
   import cv2
   from matplotlib import pyplot as plt
   
   img=cv2.imread('photo/5.jpg')
   mask = np.zeros(img.shape[:2],np.uint8)
   # cv2.imshow('img', img)
   
   bgdModel = np.zeros((1,65),np.float64)
   fgdModel = np.zeros((1,65),np.float64)
   
   rect = (100,500,421,378)
   cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)
   
   mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
   img = img*mask2[:,:,np.newaxis]
   
   plt.subplot(121), plt.imshow(img)
   plt.title("grabcut "), plt.xticks([]), plt.yticks([])
   plt.subplot(122), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
   plt.title("original "), plt.xticks([]), plt.yticks([])
   plt.show()
   cv2.waitKey(0)
   cv2.destroyAllWindows()
   ```

   这是能找到的最好用的前景检测算法了，但实际效果并不明显，因为理想图片能够检测出来，可是其压根不需要前景检测，实际图片却又检测不出来。

2. 想法是统一图片像素值，为后面的计算面积做准备。（但统一像素对腐蚀，膨胀，二值化等一系列的操作都有影响）

   - 读取照片

     ```python
     img=cv2.imread('photo/5.jpg')
     ```

   - 灰度处理。后边的操作基本都是基于灰度的。

       ```python
       gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
       ```

### 2. 对图片进行的一些试探性操作

1. 腐蚀
   ```python
   kernel=np.ones((5,5),np.uint8)
   erosion=cv2.erode(gray,kernel,iterations=5) #腐蚀
   ```

2. 膨胀：

   ```python
   kernel=np.ones((5,5),np.uint8)
   dilation=cv2.dilate(erosion,kernel,iterations=2) #膨胀
   ```

3. 模糊

   - 平滑模糊

     ```python
     blur = cv2.blur(img, (3,3))
     ```

   - 高斯模糊

     ```python
     detected_edges = cv2.GaussianBlur(gray, (3, 3), 0, ) # 高斯模糊矩阵
     ```

4. 锐化

   - 拉普拉斯锐化

     ```python
     gray_lap = cv2.Laplacian(img, cv2.CV_16S, ksize=1)
     dst = cv2.convertScaleAbs(gray_lap)
     ```

5. 二值化：

   ```python
   # OSTU二值化
   th1, ret1 = cv2.threshold(backImg, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
   ```

6. 轮廓检测：

   ```python
   contours, hierarchy = cv2.findContours(ret1, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
   ```

7. 轮廓绘制：

   - 包围盒

     ```python
     # 包围盒
     for i, contour in enumerate(contours):
         x, y, w, h = cv2.boundingRect(contour)
         cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
     
         # # 用红色表示有旋转角度的矩形框架
         # rect = cv2.minAreaRect(contours[0])
         # box = cv2.cv.BoxPoints(rect)
         # box = np.int0(box)
         cv2.drawContours(image, contour, 1, (0, 0, 255), 2)
     cv2.imshow('img', image)
     ```

   - 包围圆

     ```python
     # 包围圆
         for i, contour in enumerate(contours):
             (x, y), radius = cv2.minEnclosingCircle(contours[i])
             (x, y, radius) = np.int0((x, y, radius))  # 圆心和半径取整
             cv2.circle(image, (x, y), radius, (0, 0, 255), 2)
         cv2.imshow('img', image) 
     ```

   - 中心圆点(这个程序有点问题)

     ```python
     # 中心圆点
         for i, contour in enumerate(contours):
             rect = cv2.minEnclosingCircle(contour)
             x, y = rect[0]
             print(int(x), int(y))
             # cv2.circle(image, (int(x), int(y)), 3, (0, 255, 0), int(y))
         cv2.imshow('img', image)  
     ```

   - 拟合椭圆

     ```python
     # 拟合椭圆
         for i, contour in enumerate(contours):
             ellipse = cv2.fitEllipse(contours[i])
             cv2.ellipse(image, ellipse, (255, 255, 0), 2)
         cv2.imshow('img', image)     
     ```

8. 计算周长和面积：

   ```python
   #遍历得到最小面积的米粒
   minC=10000
   minS=10000
   for cnt in contours:
       tempS=cv2.contourArea(cnt)
       if minS>tempS:
           minS=tempS
           minC=tempC=cv2.arcLength(cnt,True)
           contour=cnt
   
   #在img中画出最小面积米粒
   cv2.drawContours(image,[contour],-1,(0,0,255,),3)
   
   maxC=-1
   maxS=-1
   for cnt in contours:
       tempS=cv2.contourArea(cnt)
       if maxS<tempS:
           maxS=tempS
           maxC=tempC=cv2.arcLength(cnt,True)
           contou=cnt
   
   #在img中画出最大面积米粒
   cv2.drawContours(image,[contou],-1,(255,0,0,),3)
   ```

### 3. 目标的识别与计数

一开始想利用绘制包围盒的方式来识别目标，计数只要统计包围圆的个数即可，但并未实现。正在尝试。

根据轮廓检测的二维数组统计目标轮廓个数。如有连通，则会视为一根钢筋，想利用连通域方法，区分出粘连的轮廓，用面积的倍数（设定阈值）来统计连通域内目标的个数，但还没做到。

只有在最理想的情况下，二值化后所有的目标轮廓都不会发生粘连，才能统计出精确的个数。


