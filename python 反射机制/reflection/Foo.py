# 动态加载的包不能把方法封装在类中，__import__ 相当于import，就相当于动态导入了整个类，调用方法时不方便
# class Foo:
def __foo():
    print('foo')
def foo1():
    print('foo1')
def foo2():
    print('foo2')
def foo3():
    print('foo3')
def foo4():
    print('foo4')
def foo5():
    print('foo5')