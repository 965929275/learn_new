调用类内的私有属性,会将被装饰类方法模拟成一个类属性。

实例：
```python
class ProtectMe(object):
    def __init__(self):
        self.me = "wangtao"
        self.__name = "私有属性"

    @property
    def name(self):
        return self.__name

if __name__ == "__main__":
    p = ProtectMe()
    print(p.name)
```
再次理解：**@property**的作用不是调用类内的私有属性，只是通过它可以实现此项功能而已（副产品），主要是将被装饰的类方法模拟成一个类属性，即：调用方法时，不用加括号了，看起来就像调用属性一样。

而此程序是在类内调用了私有属性，又用`@property`将其模拟成一个类属性，这样就可以在外部调用了。

[其他用法：菜鸟教程](http://www.runoob.com/python/python-func-property.html)

[知乎-形象的理解Class的init、self 、@staticmethod、 @classmethod、@property](https://zhuanlan.zhihu.com/p/22810357)