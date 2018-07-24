# token的使用
## 1. token是什么？
[image](https://img-blog.csdn.net/20170329111041832?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvYmx1ZXNreTEyMTU=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)

token是服务端生成的一串字符串，以作客户端进行请求的一个令牌，当第一次登录后，服务器生成一个Token便将此Token返回给客户端，以后客户端只需带上这个Token前来请求数据即可，无需再次带上用户名和密码。

## 2. 为什么使用token

为了减轻服务器的压力，减少频繁的查询数据库，使服务器更加健壮。

## 3. 怎么使用token
使用`itsdangerous生成令牌`，`TimeJSONWebSignatureSerializer`类生成具有过期时间的JSON Web签名，这个类的构造函数接受的参数是一个密钥，在程序中使用SERECT_KEY设置。

dumps()方法为指定的数据生成一个加密签名，然后再对数据和签名进行序列化，生成令
牌字符串。 expires_in 参数设置令牌的过期时间，单位为秒。

loads()方法用来解码令牌，其**唯一的参数**是令牌字符串。方法会验证签名和过期时间，如果通过，就返回原始数据，不通过则抛出异常。

```python
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from . import db

class User(UserMixin, db.Model):
# ...
    confirmed = db.Column(db.Boolean, default=False)

    #generate_confirmation_token()方法生成一个令牌，有效期默认一小时。
    def generate_confirmation_token(self, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'confirm': self.id})
    
    #confirm方法检验令牌，如果校验通过，就把confirmed属性设为True
    def confirm(self, token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return False
        if data.get('confirm') != self.id:
            return False
        self.confirmed = True
        db.session.add(self)
        return True
```
