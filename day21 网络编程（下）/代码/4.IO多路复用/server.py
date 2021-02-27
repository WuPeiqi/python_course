# ################### socket服务端 ###################
import select
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(False)  # 加上就变为了非阻塞
server.bind(('127.0.0.1', 8001))
server.listen(5)

inputs = [server, ]  # socket对象列表 -> [server, 第一个客户端连接conn ]

while True:
    # 当 参数1 序列中的socket对象发生可读时（accetp和read），则获取发生变化的对象并添加到 r列表中。
    # r = []
    # r = [server,]
    # r = [第一个客户端连接conn,]
    # r = [server,]
    # r = [第一个客户端连接conn，第二个客户端连接conn]
    # r = [第二个客户端连接conn,]
    r, w, e = select.select(inputs, [], [], 0.05)
    for sock in r:
        # server
        if sock == server:
            conn, addr = sock.accept()  # 接收新连接。
            print("有新连接")
            # conn.sendall()
            # conn.recv("xx")
            inputs.append(conn)
        else:
            data = sock.recv(1024)
            if data:
                print("收到消息：", data)
            else:
                print("关闭连接")
                inputs.remove(sock)
