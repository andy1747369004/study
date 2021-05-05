from sys import argv
from base64 import b64encode
from json import dumps
ENCODING='utf-8' # 指定编码形式
SCRIPT_NAME,IMAGE_NAME,JSON_NAME=argv # 获得文件名参数

# 以二进制读取图片，获得原始字节码，注意'rb'
with open(IMAGE_NAME,'rb')as jpg_file:
    byte_content=jpg_file.read()

base64_bytes=b64encode(byte_content) # 把原始字节码编码成base64字节码
base64_string=base64_bytes.decode(ENCODING) # 将base64字节码解码成utf-8格式的字符串

# 用字典形式保存数据
raw_data={}
raw_data['name']=IMAGE_NAME
raw_data['image_base64_string']=base64_string

json_data=dumps(raw_data,indent=2) #将字典变成json格式，缩进为2个空格

# 将 json格式的数据保存到文件中
with open(JSON_NAME,'w') as json_file:
    json_file.write(json_data)
