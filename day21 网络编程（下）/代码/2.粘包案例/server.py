import os
import json
import socket
import struct


def recv_data(conn, chunk_size=1024):
    # 获取头部信息：4字节 数据长度
    has_read_size = 0
    bytes_list = []  # 字节列表
    while has_read_size < 4:
        chunk = conn.recv(4 - has_read_size)
        has_read_size += len(chunk)
        bytes_list.append(chunk)
    header = b"".join(bytes_list)
    data_length = struct.unpack('i', header)[0]

    # 获取数据
    data_list = []
    has_read_data_size = 0
    while has_read_data_size < data_length:
        size = chunk_size if (data_length - has_read_data_size) > chunk_size else data_length - has_read_data_size
        chunk = conn.recv(size)
        data_list.append(chunk)
        has_read_data_size += len(chunk)
    data = b"".join(data_list)

    return data


def recv_file(conn, save_file_name, chunk_size=1024):
    save_file_path = os.path.join('files', save_file_name)
    # 获取头部信息：数据长度
    has_read_size = 0
    bytes_list = []
    while has_read_size < 4:
        chunk = conn.recv(4 - has_read_size)
        bytes_list.append(chunk)
        has_read_size += len(chunk)
    header = b"".join(bytes_list)
    data_length = struct.unpack('i', header)[0]

    # 获取数据
    file_object = open(save_file_path, mode='wb')
    has_read_data_size = 0
    while has_read_data_size < data_length:
        size = chunk_size if (data_length - has_read_data_size) > chunk_size else data_length - has_read_data_size
        chunk = conn.recv(size)
        file_object.write(chunk)
        file_object.flush()
        has_read_data_size += len(chunk)
    file_object.close()


def run():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # IP可复用
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    sock.bind(('127.0.0.1', 8001))
    sock.listen(5)
    while True:
        conn, addr = sock.accept()

        while True:
            # 获取消息类型
            message_type = recv_data(conn).decode('utf-8')
            if message_type == 'close':  # close
                print("关闭连接")
                break

            # 文件：{'msg_type':'file', 'file_name':"xxxx.xx" }
            # 消息：{'msg_type':'msg'}
            message_type_info = json.loads(message_type)

            if message_type_info['msg_type'] == 'msg':
                data = recv_data(conn)
                print("接收到消息：", data.decode('utf-8'))
            else:
                file_name = message_type_info['file_name']
                print("接收到文件，要保存到：", file_name)
                recv_file(conn, file_name)

        conn.close() # 四次挥手
    sock.close()


if __name__ == '__main__':
    run()
