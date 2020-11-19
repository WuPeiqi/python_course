"""
v1 = "123"
print(v1.isdecimal()) # True

v2 = "①"
print(v2.isdecimal()) # False

v3 = "123"
print(v3.isdigit()) # True

v4 = "①"
print(v4.isdigit()) # True
"""
"""
data = "武沛齐|root|wupeiqi@qq.com"
v1 = data.split("|")   # ['武沛齐', 'root', 'wupeiqi@qq.com']
print(v1)

v2 = data.split("|", 2) # ['武沛齐', 'root|wupeiqi@qq.com']
print(v2)
"""
"""
data = "武沛齐,root,wupeiqi@qq.com"

v1 = data.rsplit(',')
print(v1) # ['武沛齐', 'root', 'wupeiqi@qq.com']

v2 = data.rsplit(',',1)
print(v2) # ['武沛齐,root', 'wupeiqi@qq.com']
"""

# data = "嫂子"  # unicode，字符串类型
#
# v1 = data.encode("utf-8")  # utf-8，字节类型
# v2 = data.encode("gbk")  # gbk，字节类型
#
# print(v1)  # b'\xe5\xab\x82 \xe5\xad\x90'
# print(v2)  # b'\xc9\xa9 \xd7\xd3'


# v1 = "王老汉"
# data = v1.center(21, "-")
# print(data) #---------王老汉---------

# data = v1.ljust(21, "-")
# print(data) # 王老汉------------------

# data = v1.rjust(21, "-")
# print(data) # ------------------王老汉


# data = "alex"
# v1 = data.zfill(10)
# print(v1) # 000000alex

str







