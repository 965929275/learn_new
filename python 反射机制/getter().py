class Foo():
    _attr1 = 1
    _attr2 = 2
    attr3 = 3
    __attr4 = 4

f = Foo()

setattr(f, '_attr2', 6)
setattr(f, 'attr3', 5)

print(getattr(f, '_attr1'))
print(getattr(f, '_attr2'))

print(getattr(f, 'attr3'))
print(getattr(f, '__attr4'))

delattr(Foo, 'attr3')
try:
    print(f.attr3)
except:
    print("attr3 has gone.")

setattr(f, 'gat5', "lll")
print(f.gat5)

