#encoding:utf8
import demjson

json = '{"a":1,"b":2,"c":3,"d":4,"e":5}'

text = demjson.decode('{"a":1,"b":2,"c":3,"d":4,"e":5}')

print(text)
