# rt+

file_object = open('info.txt', mode='at+')

# 写入内容
file_object.write("武沛齐")

# 将光标位置重置起始
file_object.seek(0)

# 读取内容
data = file_object.read()
print(data)

file_object.close()
