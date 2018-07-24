# encoding:utf8
# 声明成员的访问权限

# 通知python解释器，只有这两个成员可以被调用
__all__ = ['_private_variable', 'public_teacher']

public_variable = 'hello, i am the public variable.'
_private_variable = 'hello, i am the private variable.'

def public_teacher():
    print('i am a public teacher. JAN')

def _private_teacher():
    print('i am a private teacher. CN')
