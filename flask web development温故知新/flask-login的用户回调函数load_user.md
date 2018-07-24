在`flask-login`中，有这么几行代码，虽然只有几行很容易被忽略，但是很重要。

那就是`load_user`函数：(写在User模型中)

```python
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
```

> Flask-Login 要求程序实现一个回调函数，使用指定的标识符加载用户。

回调返回一个用户，如果返回None，系统就当这个用户是匿名用户

在重载用户对象的时候reload_user方法会调用user_callback，user_id存在session中，不用重复登录

[如何理解Flask_login的user_loader回调函数？](https://www.douban.com/group/topic/78987537/)

[flask-login中的load-user何时被调用，到底有什么作用？](https://segmentfault.com/q/1010000010253582)