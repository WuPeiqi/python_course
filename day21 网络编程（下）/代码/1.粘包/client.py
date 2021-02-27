import socket
import struct

client = socket.socket()
client.connect(('127.0.0.1', 8001))

# 第一条数据
data1 = 'alex正在吃'.encode('utf-8')
header1 = struct.pack('i', len(data1))
client.sendall(header1)
client.sendall(data1)

# 第二条数据
data2 = '翔'.encode('utf-8')
header2 = struct.pack('i', len(data2))
client.sendall(header2)
client.sendall(data2)

client.close()