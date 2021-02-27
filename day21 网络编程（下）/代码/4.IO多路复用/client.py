import socket

client = socket.socket()
# 阻塞
client.connect(('127.0.0.1', 8001))


while True:
    content = input(">>>")
    if content.upper() == 'Q':
        break
    client.sendall(content.encode('utf-8'))

client.close()