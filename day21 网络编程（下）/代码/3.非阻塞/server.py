import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.setblocking(False)  # 加上就变为了非阻塞

sock.bind(('127.0.0.1', 8001))
sock.listen(5)

try:
    # 非阻塞，BlockingIOError，想要去接受一个客户端的连接。
    conn, addr = sock.accept()
except BlockingIOError as e:
    pass

# 非阻塞
client_data = conn.recv(1024)
print(client_data.decode('utf-8'))

conn.close()
sock.close()
