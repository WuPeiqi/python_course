import hashlib


def encrypt(data):
    """ 数据加密 """
    hash_object = hashlib.md5()
    hash_object.update(data.encode('utf-8'))
    return hash_object.hexdigest()


def f1():
    pass


def send_message(phone):
    data = "给{}发短信".format(phone)
    print(data)


if __name__ == '__main__':
    send_message("15131255089")
