# Python中装饰器编程


## 一、装饰器的介绍：

#### 1.什么是装饰器：

装饰器本质上其实就是一个函数，并且传入和返回的也是一个函数，可以在不改变原有函数的前提下添加额外的功能；

#### 2.装饰器的用处：

常用于**有切面需求的场景**，比如：插入日志、性能测试、事务处理、缓存、权限校验等场景。概括来说，装饰器就是为已经存在的对象添加额外的功能。

<br>

## 二、函数式装饰器：

#### 1.简单的装饰器：

首先定义一个函数`my_log`（**高阶函数**），传入的形参为`func`代表传入的**被修饰的函数**；再定义主要的修饰函数`wrapper`，执行传入的函数，并返回这个`wrapper`函数:

```python
def my_log(func):
    def wrapper(*args,**kwargs):
        print('hello')
        func(*args,**kwargs)
    return wrapper
```
这样需要被修饰的函数，就可以通过`@my_log`的方法来添加修饰的内容了：

```python
@my_log 
def world():
    print('world')
```
在运用了`*args`和`**kwargs`的组合之后，就可以修饰带有参数的函数了：

```python
@my_log 
def plus(a,b):
    print('the a + b is :{}'.format(a+b))
```

经过装饰器修饰的函数可表示为：`run = my_log(plus) = wrapper`

**注意** ：

- `*args`（无名参数）和`**kwargs`（关键字参数）两个为可变参数，两个组合可代表任何参数。

- `return wrapper`返回的是这个函数体，并不是执行后的函数体。其实返回的函数体`wrapper`，可以赋值到`a`变量上，在通过`a()`执行这个函数体；

- 在被装饰器装饰后的函数的`__name___`属性被修改为装饰器中的`wrapper`函数名，通过`functools`的`@wrap`带的装饰器可以保持函数原有的函数名：

```python
from functools import wraps

def my_log(func):
    #给传入的函数添加wraps装饰器：
    @wraps(func)
    def wrapper(*args,**kwargs):
        print('hello')
        func(*args,**kwargs)
    return wrapper
```

#### 2.带有参数的装饰器：

对原有装饰器的一个**函数封装**，并返回一个装饰器。我们可以将它理解为**一个含有参数的闭包**:

```python
def mylog_arg(label):
    def decotator(func):
        def wrapper(*args,**kwargs):
            if label == 1:
                print('This is first message!')
            elif label == 2:
                print('This is second message!')
            func(*args,**kwargs)
        return wrapper
    return decotator
```
在调用时，只需要通过`@decorator(a)`的方法就行：

```python
@mylog_arg(label=1)
def sayhello():
    print('hello world')
```
#### 3.装饰器的顺序：

如果出现多个装饰器进行装饰时，例如：

```python
@a
@b
@c
def f ():
```
顺序等效于：

```python
f = a(b(c(f)))
```
<br>

## 三、类装饰器：

#### 1.与函数式装饰器的区别：

相比函数装饰器，类装饰器具有灵活度大、高内聚、封装性等优点

#### 2.定义装饰器：

当给某个函数装饰时调用`__init__`方法，将传入的`func`赋值给`self.func`

当调用被修饰的函数时调用`__call__`的方法，执行修饰的内容和传入的函数:

```python
class Foo(object):
    def __init__(self,func):
        self.func = func    
    def __call__(self, *args, **kwargs):
        print('class decorator running')
        self.func()
        print('class decorator is end')
```
#### 3.给函数添加装饰：

和函数式装饰器类似，给需要装饰的函数添加装饰器的类名即可：

```python
@Foo 
def say_hello():
    print('hello world')
```
<br>

## 四、装饰器AOP：

#### 1.什么是AOP：

`AOP`（Aspect Oriented Program）即面向切面编程，是`OOP`（面向对象编程）的补充，就是**动态地将代码切入到类的指定方法、指定位置上的编程思想就是面向切面的编程**；

其作用可以说是把**逻辑代码**和**处理琐碎事务的代码**（例如日志）分离开，以便能够分离复杂度

>详细的AOP说明和AOP的理解可以参考资料：
>
>[什么是面向切面编程AOP？](https://www.zhihu.com/question/24863332)
>
> [轻松理解AOP思想(面向切面编程)](http://www.cnblogs.com/Wolfmanlq/p/6036019.html)

#### 2.Python中的AOP：

在`JAVA`的`Spring`框架中，`AOP`是通过反射机制（动态代理）实现的；而在`Python`中，`AOP`的思想是通过装饰器来实现的

>参考资料：
>
>[【知乎】 如何理解Python装饰器？](https://www.zhihu.com/question/26930016)