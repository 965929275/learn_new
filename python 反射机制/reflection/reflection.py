from Foo import *
import Foo

# 普通方法
class Foo1:
    def test(self,inp):
        if inp == 'foo1':
            Foo.foo1()
        elif inp == 'foo2':
            Foo.foo2()
        elif inp == 'foo3':
            Foo.foo3()
        elif inp == 'foo4':
            Foo.foo4()
        elif inp == 'foo5':
            Foo.foo5()
        else:
            print('wrong')

# 利用反射机制
class Foo2:
    def test2(self,inp):
        if hasattr(Foo,inp):
            func = getattr(Foo,inp)
            func()
            # print(func)
        else:
            print('404')

if __name__ == '__main__':
    inp = input('请输入命令：')
    # f1 = Foo1()
    # f1.test(inp)

    f2 = Foo2()
    f2.test2(inp)