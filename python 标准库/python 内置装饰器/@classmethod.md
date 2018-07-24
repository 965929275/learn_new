是一种类装饰器，用于将类中的函数修饰为类方法。
1. 此静态方法的括号中要写**cls**(class的缩写)
2. 调用此方法时同样可以用两种方法：

    - 绑定方法：实例化之后调用方法。
    - 非绑定方法：通过类直接调用。

实例：
```python
class A:
    def foo(self):
        pass

    @classmethod
    def foo1(cls):
        pass
if __name__ == "__main__":

    # 绑定方法
    a = A()
    a.foo1()

    # 非绑定方法
    A.foo1()
```