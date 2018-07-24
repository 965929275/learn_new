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