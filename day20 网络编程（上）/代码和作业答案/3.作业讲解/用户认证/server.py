import socket
import json

# 1.监听本机的IP和端口
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 8001))  # 127.0.0.1 或 查看自己局域网本地IP地址
sock.listen(5)

while True:
    # 2.等待，有人来连接（阻塞）
    conn, addr = sock.accept()

    # 3.连接成功后立即发送
    conn.sendall("欢迎使用xx系统".encode("utf-8"))

    while True:
        # 3.等待接受信息
        data = conn.recv(1024)
        if not data:
            break
        data_string = data.decode("utf-8")
        username, password = data_string.split('|')


        file_object = open("db.csv", mode='r', encoding='utf-8')

        is_success = False
        for line in file_object:
            user, pwd = line.strip().split(",")
            if user == username and pwd == password:
                is_success = True

        file_object.close()

        if is_success:
            info = {"status": True, 'msg': "登录成功"}
            conn.sendall(json.dumps(info).encode("utf-8"))
            break
        else:
            info = {"status": False, 'msg': "登录失败"}
            conn.sendall(json.dumps(info).encode("utf-8"))
    # 5.关闭与此人的连接
    conn.close()

# 6.停止服务端程序
sock.close()
