# 动态加载不导包


def test3():
    inp = input('请输入命令：')

    # 动态加载
    module,func = inp.split('/')
    print(module, func)
    obj = __import__(module)
    print(obj)

    if hasattr(obj, func):
        func = getattr(obj, func)
        func()
        # print(func)
    else:
        print('404')

if __name__ == '__main__':
    test3()