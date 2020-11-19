# 1. 请用代码实现如下进制的转换。
"""
v1 = 675  # 请将v1转换为二进制（字符串类型）。
print(bin(v1))  # "0b1010100011"

v2 = "0b11000101"  # 请将二进制v2转换为十进制（整型）
print(int(v2, base=2))  # 197

v3 = "11000101"  # 请将二进制v3转换为十进制（整型）
print(int(v3, base=2))  # 197
"""

# 2.现有 `v1=123` 和 `v2=456`，请将这两个值转换为二进制，并将其二进制中的前缀 0b 去掉，然后将两个二进制拼接起来，最终再转换为整型（十进制）。
"""
v1 = 123
v11 = bin(v1)  # "0b1111011"
v2 = 456
v21 = bin(v2)  # "0b1111011"
data = v11[2:] + v21[2:]
result = int(data, base=2)
print(result)
"""
"""
v1 = 123
v2 = 456
data = bin(v1)[2:] + bin(v2)[2:]
result = int(data, base=2)
print(result)
"""

# 3. 对第2题进行补0操作
"""
v1 = 123
v2 = 456
data = bin(v1)[2:].zfill(16) + bin(v2)[2:].zfill(16)
result = int(data,base=2)
print(result)
"""

# 4.列举你了解的那些数据类型的值转换为布尔值为False。
"""
空、0转换布尔值都是False
"""

# 5.看代码写结果
"""
456
666
345
"""

# 6.让用户输入一段文本，请实现将文本中的敏感词 `苍老师`、`波波老师`替换为 `***`，最后并输入替换后的文本。
"""
text = input("请输入内容：")
text = text.replace("苍老师", "***")
text = text.replace("波波老师", "***")
print(text)
"""

# 7.看代码写结果
"""
name = "aleX leNb "
print(name.strip())

print(name.startswith("al"))
print(name[0:2] == "al")

print(name.endswith("Nb"))
print(name[-2:] == "Nb")

v1 = name.replace("l", "p")
print(v1)

v2 = name.split("l")
print(v2)  # ['a', 'eX ', 'eNb ']

v3 = name.split("l", 1)
print(v3)  # ['a', 'eX leNb ']

print(name.upper())
print(name.lower())
"""

# 8.如何实现字符串的翻转？[面试题]
"""
name = "武沛齐"
data = name[::-1]
print(data)
"""

# 9.有字符串s = "123a4b5c"
"""
s = "123a4b5c"

print(s[0:3])
print(s[3:6])

print(s[-1])
print(s[len(s) - 1])

print(s[-3:0:-2])
"""

# 10. while + 索引
"""
message = "伤情最是晚凉天，憔悴厮人不堪言"
index = 0
while index < len(message):
    print(message[index])
    index += 1
"""

# 11 for循环
"""
message = "伤情最是晚凉天，憔悴厮人不堪言"
for item in message:
    print(item)
"""

# 12.for循环+range+索引
"""
message = "伤情最是晚凉天，憔悴厮人不堪言"
for index in range(len(message)):
    print( message[index] )
"""

# 13.使用for循环实现输出倒计时效果，例如：输出内容依次是："倒计时3秒"，"倒计时2秒"，"倒计时1秒"。
"""
for num in range(3, 0, -1):  # [3,2,1]
    text = "倒计时{}秒".format(num)
    print(text)
"""

# 14.让用户输入一段文本，请计算文本中 "浪" 出现的次数，并输入结果。
"""
text = input("请输入一段文本：") # 阿士大夫埃里克森打发斯蒂芬
count = 0
for item in text:
    if item == "浪":
        count += 1
print(count)
"""

# 15.获取用户两次输入的内容，并提取其中的数字，然后实现数字的相加（转换为整型再相加）
"""
num1 = input("请输入：")  # "asdfd123sf2312"
num1_list = []
for item in num1:
    if item.isdecimal():
        num1_list.append(item)
data1 = "".join(num1_list)  # "1232312"

num2 = input("请输入：")  # a12dfd183sf23
num2_list = []
for item in num2:
    if item.isdecimal():
        num2_list.append(item)
data2 = "".join(num2_list)

result = int(data1) + int(data2)
print(result)
"""

"""
num1 = input("请输入：")  # "asdfd123sf2312"
data1 = ""
for item in num1:
    # "a" "s" "1" "2" ...
    if item.isdecimal():
        data1 += item

num2 = input("请输入：")  # "asdfd123sf2312"
data2 = ""
for item in num2:
    # "a" "s" "1" "2" ...
    if item.isdecimal():
        data2 += item

result = int(data1) + int(data2)
print(result)
"""