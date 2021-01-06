from utils.email import send_email
from config import settings


def login():
    print("欢迎使用用户登录")


def register():
    print("欢迎使用用户注册")
    user = input("请输入用户名：")
    pwd = input("请输入密码：")
    email = input("请输入邮箱：")

    user_string = "{}|{}|{}\n".format(user, pwd, email)
    with open(settings.USER_DB_PATH, mode='a', encoding='utf-8') as file_object:
        file_object.write(user_string)
        file_object.flush()
    message = "恭喜{}，注册成功，您的密码为：{}".format(user, pwd)
    send_email("用户注册", message, email)
    print("注册成功")


def start():
    func_dict = {
        "1": {'title': "登录", 'func': login},
        "2": {'title': "注册", 'func': register},
    }

    tips = ";".join(["{}.{}".format(k, v['title']) for k, v in func_dict.items()])
    print(tips)

    choice = input("请选择序号：")

    func_dict = func_dict.get(choice)
    if not func_dict:
        print("选择错误")
        return
    func_dict['func']()
