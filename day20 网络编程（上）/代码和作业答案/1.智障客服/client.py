import socket

# 1. 向指定IP发送连接请求
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8001))

# 2.连接成功后，获取系统登录信息
message = client.recv(1024)
print(message.decode("utf-8"))

while True:
    content = input("请输入(q/Q退出)：")
    if content.upper() == 'Q':
        break
    client.sendall(content.encode("utf-8"))

    # 3. 等待，消息的回复
    reply = client.recv(1024)
    print(reply.decode("utf-8"))

# 关闭连接，关闭连接时会向服务端发送空数据。
client.close()