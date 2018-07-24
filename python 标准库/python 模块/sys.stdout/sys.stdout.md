改变输出流：

```shell
λ python
>>> f = open('test.md', 'w')
>>> import sys
>>> sys.stdout = f
>>> print('learn python sys.stdout')
>>> f.close()
>>> exit()
```

