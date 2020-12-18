"""
# 1.打开文件
# 	路径：t1.txt
#   模式：wb（要求写入的内容需要是字节类型）
file_object = open("t1.txt", mode='wb')

# 2.写入内容
file_object.write("武沛齐".encode("utf-8"))

# 3.文件关闭
file_object.close()
"""

"""
file_object = open("t2.txt", mode='wt', encoding='utf-8')

file_object.write("武沛齐")

file_object.close()
"""

"""
f1 = open('a1.png',mode='rb')
content = f1.read()
f1.close()

f2 = open('a2.png',mode='wb')
f2.write(content)
f2.close()
"""








