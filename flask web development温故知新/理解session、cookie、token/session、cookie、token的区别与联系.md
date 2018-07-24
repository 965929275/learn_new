首先，HTTP协议是一个**匿名的、无状态的**请求响应协议
## cookie与session原理：
当浏览器（Browser）向服务器（Server）发送一个请求（request）时，服务器会生成一个cookie和一个session，session保存在服务器端，cookie以key：value的形式存储，key一般为唯一的sessionID，服务器返回一个响应（Response）给浏览器，并携带cookie，浏览器就会将cookie保存下来。当下一次访问服务器时，请求会携带cookie发送到服务器，服务器就会解析这个cookie，如果sessionID对应的value值与服务器端保存的value值相等，则验证了用户的身份。

## token（令牌）原理：

1.用户登录校验，校验成功后就返回Token给客户端。

2.客户端收到数据后保存在客户端

3.客户端每次访问API是携带Token到服务器端。

4.服务器端采用filter过滤器校验。校验成功则返回请求数据，校验失败则返回错误码

用于验证用户身份，多用于第三方，相当于一个字段，可以在代码中显示调用。存储在客户端中。

[我的有道云笔记](http://note.youdao.com/noteshare?id=bcaf498744e5a211519424e1dc7dd062&sub=wcp1522898001744770)