[知乎-使用opencv训练分类器](https://zhuanlan.zhihu.com/p/26390670)

[阿里云-如何用 OpenCV 训练自己的分类器 ](https://yq.aliyun.com/articles/9334#)

[opencv 实时识别指定物体](https://blog.csdn.net/qq_27063119/article/details/79247266)

[利用 opencv 训练基于 Haar 特征、LBP 特征、Hog 特征的分类器 cascade.xml](https://blog.csdn.net/lql0716/article/details/72566839)

[OpenCV 实践之路——人脸检测（C++/Python)](https://blog.csdn.net/xingchenbingbuyu/article/details/51105159)

[制作样本的注意事项](https://blog.csdn.net/liulina603/article/details/8184451)

### 1.创建样本

#### 正样本

待检测的样本。

对于正样本，通常的做法是先把所有正样本裁切好，并对尺寸做规整（即缩放至指定大小）（20*20）

1. 将制作好的正样本放入指定文件夹

2. 使用**cmd**进入负样本所在文件夹

3. `dir /b > info.txt`

4. 会生成一个**info.txt**描述文件

5. 进入info.dat文件，删除最后一行`info.txt`(可能不在最后一行)

6. 在每一行后边添加指定数字：eg:`1.bmp 1 0 0 20 20`

   bmp 后面那五个数字分别表示**图片个数**，**目标的起始位置** **宽高**。这样就生成了正样本描述文件 info.dat。 

#### 负样本

负样本可以来自于任意的图片，但这些图片不能包含目标特征。 负样本由背景描述文件来描述。背景描述文件是一个文本文件，每一行包含了一个负样本图片的文件名（基于描述文件的相对路径）。该文件创建方法如下： 

1. 将制作好的负样本放入指定文件夹

2. 使用**cmd**进入负样本所在文件夹

3. `dir /b > info.txt `

4. 会生成一个**info.txt**描述文件

5. 进入info.dat文件，删除最后一行`info.txt`

### 2.训练分类器

#### 1. 生成样本

*正样本需要生成txt描述文件和vec文件，负样本只需要生成txt描述文件*

*要使用很多dll，自行百度安装即可。*

训练样本集需要使用opencv自带的软件：createsamples（没有的话，自行百度）

**createsamples 具体训练参数如下：**

> - vec <vec_file_name> 训练好的正样本的输出文件名。
> - img<image_file_name> 源目标图片（例如：一个公司图标）
> - bg<background_file_name> 背景描述文件。
> - num<number_of_samples> 要产生的正样本的数量，和正样本图片数目相同。
> - bgcolor<background_color> 背景色（假定当前图片为灰度图）。背景色制定了透明色。对于压缩图片，颜色方差量由 bgthresh 参数来指定。则在 bgcolor－bgthresh 和 bgcolor＋bgthresh 中间的像素被认为是透明的。
> - bgthresh<background_color_threshold>
> - inv 如果指定，颜色会反色
> - randinv 如果指定，颜色会任意反色
> - maxidev<max_intensity_deviation> 背景色最大的偏离度。
> - maxangel<max_x_rotation_angle>
> - maxangle<max_y_rotation_angle>，
> - maxzangle<max_x_rotation_angle> 最大旋转角度，以弧度为单位。
> - show 如果指定，每个样本会被显示出来，按下 "esc" 会关闭这一开关，即不显示样本图片，而创建过程继续。这是个有用的 debug 选项。
> - w<sample_width> 输出样本的宽度（以像素为单位）
> - h<sample_height> 输出样本的高度，以像素为单位。
> - 注：正样本也可以从一个预先标记好的图像集合中获取。这个集合由一个文本文件来描述。每一个文本行对应一个图片。每行的第一个元素是图片文件名，第二个元素是对象实体的个数。后面紧跟着的是与之匹配的矩形框（x, y, 宽度，高度）。

找到 opencv_createsamples.exe，把它放进训练集目录中，在cmd输入 

```shell
 opencv_createsamples.exe -info info.txt -vec pos.vec -num 120 -w 20 -h 20
```

参数说明：

opencv_createsamples.exe **-info** [正样本描述文件（绝对路径）] **-vec** [生成的vec文件目录（绝对路径）] **-num** [正样本数目] **-w** [样本宽] **-h** [样本高]

#### 2. 正式训练

**Haartraining 的命令行参数如下： **
> - data<dir_name>     存放训练好的分类器的路径名。 
>
>- vec<vec_file_name>     正样本文件名（由 trainingssamples 程序或者由其他的方法创建的） 
>- bg<background_file_name>     背景描述文件。 
>- npos<number_of_positive_samples>， 
>- nneg<number_of_negative_samples>     用来训练每一个分类器阶段的正 / 负样本。合理的值是：nPos = 7000;nNeg = 3000 
>- nstages<number_of_stages>     训练的阶段数。 
>- nsplits<number_of_splits>     决定用于阶段分类器的弱分类器。如果 1，则一个简单的 stump classifier 被使用。如果是 2 或者更多，则带有 number_of_splits 个内部节点的 CART 分类器被使用。 
>- mem<memory_in_MB>     预先计算的以 MB 为单位的可用内存。内存越大则训练的速度越快。 
>- sym（default） －nonsym     指定训练的目标对象是否垂直对称。垂直对称提高目标的训练速度。例如，正面部是垂直对称的。 
>- minhitrate<min_hit_rate>     每个阶段分类器需要的最小的命中率。总的命中率为 min_hit_rate 的 number_of_stages 次方。 
>- maxfalsealarm<max_false_alarm_rate>     没有阶段分类器的最大错误报警率。总的错误警告率为 max_false_alarm_rate 的 number_of_stages 次方。 
>- weighttrimming<weight_trimming>     指定是否使用权修正和使用多大的权修正。一个基本的选择是 0.9 －eqw －mode<basic(default)|core|all>     选择用来训练的 haar 特征集的种类。basic 仅仅使用垂直特征。all 使用垂直和 45 度角旋转特征。 
>- w<sample_width> －h<sample_height>     训练样本的尺寸，（以像素为单位）。必须和训练样本创建的尺寸相同。 

找到 opencv_haartraining.exe 文件，放入训练集目录中，在cmd中输入：

```shell
opencv_haartraining.exe -data e:\test\data0\cascade0 -vec e:\test\posdata0\pos.vec -bg e:\test\negdata0\negdata0.txt -npos 120 -nneg 120 -nsplits 2 -mem 512 -nonsym -w 20 -h 20 -minpos 100 -nstages 4
```

参数说明：

opencv_haartraining.exe **-data** [生成的分类器的存放目录（绝对路径）] **-vec** [正样本的vec文件目录（绝对路径）] **-bg** [负样本的描述文件目录（绝对路径）] **-npos** [每级分类器训练时所用到的正样本数目] **-nneg** [每级分类器训练时所用到的负样本数目 ] **-nsplits** [] **-mem** [] **-nonsym** **-w** [宽] **-h** [高] **-minpos** [] **-nstage** []

- **-numPos**  每级分类器训练时所用到的正样本数目，应小于 vec 文件中正样本的数目，具体数目限制条件为：numPos+（numStages-1）*numPos*（1-minHitRate）<=vec 文件中正样本的数目
- **-numNeg ** 每级分类器训练时所用到的负样本数目，可以大于 - bg 指定的图片数目
- **-numStages ** 训练分类器的级数，强分类器的个数
- **-nspilts** 不知道
- **-mem** 缓存器大小
- **-minpos** 
- **-nstage** 

我成功运行的命令：

```shell
opencv_haartraining.exe -data C:\Users\96592\Desktop\Haar -vec C:\Users\96592\Desktop\Haar\posative\pos.vec -bg C:\Users\96592\Desktop\Haar\negative\neg.txt -npos 58 -nneg 181 -nstages 15 -mem 1024 -mode ALL -w 40 -h 40
```

#### 3. 生成xml文件

网上有两种方法。

我使用的`convert_cascade --size="40*40" C:\Users\96592\Desktop\Haar haar.xml`来生成xml文件。

参数说明：

- --size=“40*40”：这是正样本的分辨率
- C:\Users\96592\Desktop\Haar：生成的xml文件的路径（貌似不管事，直接在运行convert_cascade的地方生成了xml）
- haar.xml：生成的分类器

复制粘贴xml到指定的地方，载入程序就可以使用了。

### 3.使用训练好的样本集进行检测

主要就是将训练好的分类器载入程序，进行识别，程序中可以载入多个分类器，从而识别不同的区域。

```python
# encoding:utf8
import cv2

cascade = cv2.CascadeClassifier("haar.xml")

img = cv2.imread("photo/12.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

irons = cascade.detectMultiScale(gray, 1.1, 5, cv2.CASCADE_SCALE_IMAGE, (50, 50), (100, 100))

print(len(irons)) # 目标数量

if len(irons) > 0:
    for i,faceRect in enumerate(irons):
        x, y, w, h = faceRect
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2, 8, 0)
        cv2.putText(img, "#{}".format(i + 1), (int(x), int(y) - 15), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 1)  # 左上角坐标
cv2.imwrite("cat2.jpg", img, [int(cv2.IMWRITE_JPEG_QUALITY), 100]) # 保存图片
cv2.imshow("img", img)
cv2.waitKey(0)
```



