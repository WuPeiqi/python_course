import socket
import json

# 1. 向指定IP发送连接请求
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8001))

# 2.连接成功后，获取系统登录信息
message = client.recv(1024)
print(message.decode("utf-8"))

while True:
    user = input("请输入用户名：")
    pwd = input("请输入密码：")
    content = "{}|{}".format(user, pwd)
    client.sendall(content.encode("utf-8"))

    reply = client.recv(1024)
    info = json.loads(reply.decode("utf-8"))
    if info['status']:
        print(info['msg'])  # 登录成功
        break
    else:
        print(info['msg'])  # 登录失败
# 关闭连接
client.close()
