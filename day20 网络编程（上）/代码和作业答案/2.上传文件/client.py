import time
import os
import socket

client = socket.socket()
client.connect(('127.0.0.1', 8001))

file_path = input("请输入要上传的文件：")

# 先发送文件大小
file_size = os.stat(file_path).st_size
client.sendall(str(file_size).encode('utf-8'))

print("准备...")
time.sleep(2)
print("开始上传..")
file_object = open(file_path, mode='rb')
read_size = 0
while True:
    chunk = file_object.read(1024) # 每次读取1024字节
    client.sendall(chunk)
    read_size += len(chunk)
    if read_size == file_size:
        break

client.close()