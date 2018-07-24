#encoding:utf8
import json

jsonData = '{"a":1,"b":2,"c":3,"d":4,"e":5}'
# 字典中key为单引号，json中key为双引号
# dict：{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# json：{"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}

text = json.loads(jsonData)

print(type(text))  # <class 'dict'>
print(text)
