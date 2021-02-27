import os
import json
import socket
import struct


def send_data(conn, content):
    data = content.encode('utf-8')
    header = struct.pack('i', len(data))
    conn.sendall(header)
    conn.sendall(data)


def send_file(conn, file_path):
    file_size = os.stat(file_path).st_size
    header = struct.pack('i', file_size)
    conn.sendall(header)

    has_send_size = 0
    file_object = open(file_path, mode='rb')
    while has_send_size < file_size:
        chunk = file_object.read(2048)
        conn.sendall(chunk)
        has_send_size += len(chunk)
    file_object.close()


def run():
    client = socket.socket()
    client.connect(('127.0.0.1', 8001))

    while True:
        """
        请发送消息，格式为：
            - 消息：msg|你好呀
            - 文件：file|xxxx.png
        """
        content = input(">>>")  # msg or file

        if content.upper() == 'Q':
            send_data(client, "close")
            break

        input_text_list = content.split('|')
        if len(input_text_list) != 2:
            print("格式错误，请重新输入")
            continue

        message_type, info = input_text_list

        # 发消息
        if message_type == 'msg':

            # 发消息类型
            send_data(client, json.dumps({"msg_type": "msg"}))

            # 发内容
            send_data(client, info)

        # 发文件
        else:
            file_name = info.rsplit(os.sep, maxsplit=1)[-1] # / 分割  \

            # 发消息类型
            send_data(client, json.dumps({"msg_type": "file", 'file_name': file_name}))

            # 发内容
            send_file(client, info)

    client.close() # 四次挥手，发送空数据


if __name__ == '__main__':
    run()
