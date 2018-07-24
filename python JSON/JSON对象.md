# JSON对象
## 对象语法
```
{ "name":"runoob", "alexa":10000, "site":null }
```
- JSON对象使用在大括号({})中书写。
- 对象可以包含多个键值对。
- key必须是字符串，value可以是合法的JSON数据类型（字符串，数字，对象，数组，布尔值，null）
- key和value使用 ":" 分离
- 每个键值对使用 "," 分离

## 访问对象值
1. 使用 "." 访问对象的值。
```
var myObj, x;
myObj = { "name":"runoob", "alexa":10000, "site":null };
x = myObj.name;
```
2. 使用 "[]" 访问对象的值。
```
var myObj, x;
myObj = { "name":"runoob", "alexa":10000, "site":null };
x = myObj["name"];
```
## 循环对象
1. 使用 for-in 来循环对象的属性
```
var myObj = { "name":"runoob", "alexa":10000, "site":null };
for (x in myObj) {
    document.getElementById("demo").innerHTML += x + "<br>";
}
```
2. 循环对象的属性时，可以使用 "[]" 访问属性的值
```
var myObj = { "name":"runoob", "alexa":10000, "site":null };
for (x in myObj) {
    document.getElementById("demo").innerHTML += myObj[x] + "<br>";
}
```
**访问属性的值时，[]跟随的是整个JSON对象的变量名，而不是属性名**

**这里是通过直接访问value值来进行迭代的，有点类似于循环数组**

## 嵌套JSON对象
JSON对象中可以包含另一个JSON对象：
```
myObj = {
    "name":"runoob",
    "alexa":10000,
    "sites": {
        "site1":"www.runoob.com",
        "site2":"m.runoob.com",
        "site3":"c.runoob.com"
    }
}
```
你可以使用点号(.)或者中括号([])来访问嵌套的 JSON 对象。
```
x = myObj.sites.site1;
// 或者
x = myObj.sites["site1"];
// 或者
x = myObj["sites"]["site1"];
// 或者
x = myObj["sites"].site1;
```
## 修改值
访问属性的值后，用赋值的方式进行覆盖。
## 删除对象属性
使用**delete**关键字删除对象的属性,访问对象属性时，上述四种方法都行
```
delete myObj.sites.site1;
```

```
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>菜鸟教程(runoob.com)</title>
</head>
<body>

<p>删除 JSON 对象属性。</p>

<p id="demo"></p>

<script>
var myObj, i, x = "";
myObj = {
    "name":"runoob",
    "alexa":10000,
    "sites": {
        "site1":"www.runoob.com",
        "site2":"m.runoob.com",
        "site3":"c.runoob.com"
    }
}
// 删除
delete myObj.sites.site1;
// 循环打印
for (i in myObj.sites) {
    x += myObj.sites[i] + "<br>";
}

document.getElementById("demo").innerHTML = x;

</script>

</body>
</html>
```