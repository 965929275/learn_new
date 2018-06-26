# 理解python反射机制

## 面对的对象

首先，要说明的是，反射机制不是每种语言都有的，它仅仅面对**动态语言**

### 动态语言

>动态语言，是指程序在运行时可以改变其结构：新的函数可以被引进，已有的函数可以被删除等在结构上的变化，类型的检查是在运行时做的，优点为方便阅读，清晰明了，缺点为不方便调试。
>- 中文名：动态语言
>- 含    义：是指程序在运行时可以改变其结构
>- 优    点：方便阅读，清晰明了
>- 缺    点：不方便调试
>
>——摘自百度百科

#### 常见的动态语言

Java（准动态）、JavaScript、python

#### 常见的静态语言

C、C++

## 反射机制是什么？

> JAVA反射机制是在运行状态中，对于任意一个类，都能够知道这个类的所有属性和方法；对于任意一个对象，都能够调用它的任意方法和属性；这种动态获取信息以及动态调用对象方法的功能称为java语言的反射机制。 
>
> ——摘自百度百科

### 理解反射机制

由于网上找不到关于python反射机制的科学定义，只好自己理解了。借鉴Java反射机制。

我认为反射机制就是**动态地获取任意类的任意属性及方法**，不管它是公有的，还是私有的，都能获取到。

### 理解自省机制



## 为什么要使用反射机制（使用场景）

- 框架利用反射机制来够获得程序员自己写的类的基本结构
- 获取任意类的任意属性及方法



### 自省机制举例

- dir()函数查看所有属性和参数列表

- python2中：**getattr()**方法，传入参数是该对象的函数或者属性的名字，返回对象的函数或者属性实例。

  ```powershell
  >>> getattr(string,'split')
  <function split at 0x000000000391A208>
  ```

- python2中：**allable()**方法，如果传入的参数是可以调用的函数，则返回true，否则返回false。 

  ```shell
  >>> callable(getattr(string,'split'))
  True
  >>> callable(getattr(string,'__doc__'))
  False
  ```

*列出对象的所有函数：*

`methodList = [method for method in dir(object) if callable(getattr(object,method))]`

```shell
>>> methodList = [method for method in dir(string) if callable(getattr(string,method))]
>>> print methodList
['Formatter', 'Template', '_TemplateMetaclass', '_float', '_int', '_long', '_multimap', 'atof', 'atof_error', 'atoi', 'atoi_error', 'atol', 'atol_error', 'capitalize', 'capwords', 'center', 'count', 'expandtabs', 'find', 'index', 'index_error', 'join', 'joinfields', 'ljust', 'lower', 'lstrip', 'maketrans', 'replace', 'rfind', 'rindex', 'rjust', 'rsplit', 'rstrip', 'split', 'splitfields', 'strip', 'swapcase', 'translate', 'upper', 'zfill']
```

### python体现反射

**python2中：**

**globals()**方法：返回一个map，这个map的key是全局范围内对象的名字，value是该对象的实例。

  ```shell
  >>> globals()
  {'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, '__package__': None}
  ```

  导入**sys**后：

  ```shell
  >>> import sys
  >>> globals()
  {'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', 'sys': <module 'sys' (built-in)>, '__doc__': None, '__package__': None}
  ```

  如果导入类，在map中，可以找到类：

  ```shell
  >>> from os import urandom
  >>> globals()
  {'__builtins__': <module '__builtin__' (built-in)>, '__package__': None, 'sys': <module 'sys' (built-in)>, 'urandom': <built-in function urandom>, '__name__': '__main__', 'os': <module 'os' from 'C:\Python\Python27\lib\os.pyc'>, '__doc__': None}
  ```

返回的是字典类型，就可以通过**类名（key）**找到**类（value）**了

如果要实例化对象，将获得的类赋值给一个变量即可

**这不就是另一种实例化对象的方法了吗，是吧**

----

**globals()**方法使用时需要提前导入相应的模块，不导入则会抛出异常。

所以有了另一种**动态导入**的方法：

`__import__`函数：传入的参数是module的名字，返回这个module，然后利用**getattr()**方法实现对象的实例化：

```shell
>>> model =  __import__('sys')
>>> print(model)
<module 'sys' (built-in)>
```

经验证，以上两种方法python3同样适用

借鉴自[Python 反射机制](http://blog.chinaunix.net/uid-9687384-id-1998500.html)

## 用代码实现

`reflection`

[简书-Python-反射机制](https://www.jianshu.com/p/80b544c2b82d)

----

----

后记：python的内置函数：[getattr](http://www.runoob.com/python/python-func-getattr.html) [hasattr](http://www.runoob.com/python/python-func-hasattr.html) [setattr](http://www.runoob.com/python/python-func-setattr.html) [delattr](http://www.runoob.com/python/python-func-delattr.html)基本上完整地实现了python的反射机制，`__import__`实现了动态导入。

