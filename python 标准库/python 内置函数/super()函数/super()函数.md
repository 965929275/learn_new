[菜鸟教程：super()函数](http://www.runoob.com/python/python-func-super.html)

## 是什么&为什么
1. 当父类中的方法被重写，而又想**在子类中重新调用父类中的方法**时，就可以在子类中使用super()函数。（因为父类的方法被重写时，只是在子类中被覆盖了而已，父类中原本的方法并没有消失）

## 使用方法
1. Python3.x 和 Python2.x 的一个区别是: Python 3 可以使用直接使用 super().xxx 代替 super(Class, self).xxx

python3实例：
```python
class A:
    def __init__():
        pass

class B(A):
    def __init__():
        pass
    super().__init__()  # 调用了父类的方法
```
python2实例：
```python
class A(object):
    def __init__():
        pass

class B(A):
    def __init__():
        pass
    super(B, self).__init__()  # 调用了父类的方法
```
