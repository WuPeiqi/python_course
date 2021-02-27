import socket

# 1.监听本机的IP和端口
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 8001))
sock.listen(5)

while True:
    # 2.等待，有人来连接（阻塞）
    conn, addr = sock.accept()

    while True:
        # 3.等待，连接者发送消息（阻塞）
        client_data = conn.recv(1024)
        print(client_data)
        if not client_data: # 客户端断开连接
            break

    # 5.关闭连接
    conn.close()

# 6.停止服务端程序
sock.close()