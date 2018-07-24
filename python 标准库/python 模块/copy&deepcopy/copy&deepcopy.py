# encoding:utf8
import copy

class MyCopy():
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return str(self.value)

foo = MyCopy(7)

a = ['foo', foo]
b = a[:]
c = list(a)
d = copy.copy(a)      # ['foo', 17]
e = copy.deepcopy(a)  # ['foo', 7]

a.append('abc')
foo.value = 17

print(e)
