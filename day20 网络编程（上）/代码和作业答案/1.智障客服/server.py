import socket

# 1.监听本机的IP和端口
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 8001))  # 127.0.0.1 或 查看自己局域网本地IP地址
sock.listen(5)

while True:
    # 2.等待，有人来连接（阻塞）
    conn, addr = sock.accept()
    # 3.连接成功后立即发送
    conn.sendall("欢迎使用xx系统，请输入您想要办理的业务！".encode("utf-8"))

    while True:
        # 3.等待接受信息
        data = conn.recv(1024)
        if not data:
            break
        data_string = data.decode("utf-8")
        print("客户端提问：",data_string)
        # 4.回复消息
        conn.sendall("你说啥？".encode("utf-8"))

    print("断开连接了")
    # 5.关闭与此人的连接
    conn.close()

# 6.停止服务端程序
sock.close()

