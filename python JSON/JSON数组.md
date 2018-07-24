# JSON数组
## 数组作为JSON对象
```
[ "Google", "Runoob", "Taobao" ]
```
- JSON数组在中括号中书写。
- JSON中数组值必须是合法的JSON数据类型（字符串、数字、对象、数组、布尔值、null）
- JavaScript 中，数组值可以是以上的 JSON 数据类型，也可以是 JavaScript 的表达式，包括函数，日期，及 undefined。

## JSON对象中的数组
对象属性的值可以是一个数组：
```
{
"name":"网站",
"num":3,
"sites":[ "Google", "Runoob", "Taobao" ]
}
```
可以利用索引访问数组：
```
x = myObj.sites[0];
// 或者
x = myObj["sites"][0];
```
## 循环数组
1. for-in访问数组
```
for (i in myObj.sites) {
    x += myObj.sites[i] + "<br>";
}
```
2. for循环遍历数组
```
for (i = 0; i < myObj.sites.length; i++) {
    x += myObj.sites[i] + "<br>";
}
```
## 嵌套JSON对象中的数组
JSON对象数组可以包含另一个数组，或者另一个JSON对象。
```
myObj = {
    "name":"网站",
    "num":3,
    "sites": [
        { "name":"Google", "info":[ "Android", "Google 搜索", "Google 翻译" ] },
        { "name":"Runoob", "info":[ "菜鸟教程", "菜鸟工具", "菜鸟微信" ] },
        { "name":"Taobao", "info":[ "淘宝", "网购" ] }
    ]
}
```
==此例子为： 对象(数组(对象(数组)))==

使用for-in循环访问每个数组：
```
for (i in myObj.sites){
    x += "<h1>" + myObj.sites[i].name + "</h1>";
    for (j in myObj.sites[i].info){
        x += myObj.sites[i].info[j] + "<br>";
    }
}
```
## 修改数组元素
先访问在赋值。
```
myObj.sites[1] = "Github";
```
## 删除数组元素
**delete**关键字删除数组元素：
```
delete myObj.sites[1];
```