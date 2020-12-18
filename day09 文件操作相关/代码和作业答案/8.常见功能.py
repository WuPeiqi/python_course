f = open('info.txt', mode='rb')

p1 = f.tell()
print(p1)  # 0

f.read(3)  # 读3个字节

p2 = f.tell()
print(p2)  # 3

f.close()
