import socket

# 1. 向指定IP发送连接请求
client = socket.socket()
client.connect(('127.0.0.1', 8001))  # 向服务端发起连接（阻塞）10s

# 2. 连接成功之后，发送消息
client.sendall('hello'.encode('utf-8'))

# 3. 等待，消息的回复（阻塞）
reply = client.recv(1024)
print(reply)

# 4. 关闭连接
client.close()
