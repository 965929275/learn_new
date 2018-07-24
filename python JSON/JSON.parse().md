# JSON.parse()
在接收服务器数据时一般是字符串。

使用 JSON.parse() 方法将数据转换为 JavaScript 对象。

语法：

`JSON.parse(text[, reviver])`

参数说明：
- **text**：必须，一个有效的字符串。
- **reviver**：可选，一个转换结果的函数， 将为对象的每个成员调用此函数。

## JSON解析实例
服务器端的JSON数据：
```
{ "name":"runoob", "alexa":10000, "site":"www.runoob.com" }

```
使用 JSON.parse() 方法处理以上数据，将其转换为 JavaScript 对象：
```
var obj = JSON.parse('{ "name":"runoob", "alexa":10000, "site":"www.runoob.com" }');
```
*解析前要确保你的数据是标准的 JSON 格式，否则会解析出错。*

*可以用在线工具检测*

----

解析完成后，前端就可以使用这些JSON数据了。
## 从服务器端接收JSON数据：
可以使用 AJAX 从服务器请求 JSON 数据，并解析为 JavaScript ==对象==。
## 从服务端接收数组的 JSON 数据

如果从服务端接收的是数组的 JSON 数据，则 JSON.parse 会将其转换为 JavaScript ==数组==

## 异常

### 解析数据

JSON不能存储 Date 对象，需要先转化为字符串在存储。之后在将字符串转化为 Date 对象。

### 解析函数

JSON 不允许包含函数，但你可以将函数作为字符串存储，之后再将字符串转换为函数。

不建议在 JSON 中使用函数。

----


[更多内容请看菜鸟](http://www.runoob.com/json/json-parse.html)