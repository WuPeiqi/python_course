# 字符串类型
name = "武沛齐"
print(name) # 武沛齐
# 字符串转换为字节类型
data = name.encode("gbk")
# print(data) # b'\xe6\xad\xa6\xe6\xb2\x9b\xe9\xbd\x90'  utf8，中文3个字节
print(data) # b'\xce\xe4\xc5\xe6\xc6\xeb'              gbk，中文2个字节

# 把字节转换为字符串
old = data.decode("gbk")
print(old)