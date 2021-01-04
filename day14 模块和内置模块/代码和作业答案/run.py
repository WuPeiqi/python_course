from commons.utils import encrypt, send_message


def handler():
    # ....
    phone = input("请输入手机号：")
    send_message(phone)
    # ....


if __name__ == "__main__":
    handler()
