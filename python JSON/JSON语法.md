# JSON语法
JSON语法时JavaScript语法的子集。
## JSON语法规则
- 数据在名称/值对中
- 数据由逗号分离
- 大括号保存对象
- 中括号保存数组

## JSON名称/值对
名称/值对包括字段名称（在双引号中），后面写一个冒号，然后是值：
```
"name" : "菜鸟教程"
```
等价于JavaScript语句：
```
name = "菜鸟教程"
```
## JSON值
- 数字（整数或浮点数）
- 字符串（双引号内）
- 逻辑值（true或false）
- 数组（中括号内）
- 对象（大括号内）
- null

## JSON对象
JSON对象在大括号{}中，可以包含多个名称/值对。
```
{ "name":"菜鸟教程" , "url":"www.runoob.com" }
```
等价于JavaScript语句：
```
name = "菜鸟教程"
url = "www.runoob.com"
```
## JSON数组
在中括号中书写，数组可以包含多个对象：
```
{
"sites": [
{ "name":"菜鸟教程" , "url":"www.runoob.com" }, 
{ "name":"google" , "url":"www.google.com" }, 
{ "name":"微博" , "url":"www.weibo.com" }]
}
```
对象“sites”是包含三个对象的数组，每个对象代表一条关于某个网站（name,url）的记录。
## JSON布尔值
```
{ "flag":true }
```
## JSON null
JSON可以设置null值：
```
{ "runoob":null }
```
## JSON文件
- JSON文件的文件类型是“.json”
- JSON 文本的 MIME 类型是 "application/json"