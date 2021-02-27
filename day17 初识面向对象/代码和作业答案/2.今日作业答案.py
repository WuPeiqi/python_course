# 1. 简述面向对象三大特性?
"""
- 封装，将方法封装到类中 或 将数据封装到对象中，便于以后使用。
- 继承，将类中的公共的方法提取到基类中去实现。
- 多态，Python默认支持多态（这种方式称之为鸭子类型），最简单的基础下面的这段代码即可。
    def func(arg):
        v1 = arg.copy() # 浅拷贝
        print(v1)
"""

# 2.将以下函数改成类的方式并调用
"""
class Foo(object):

    def func(self, a1):
        print(a1)


obj = Foo()
obj.func("武沛齐")
"""

# 3. 面向对象中的self指的是什么?
"""
self是一个参数，在通过 对象.方法 的方式去执行方法时，这个参数会被python自动传递（值为调用当前方法的对象）
"""

# 4.以下代码体现 向对象的什么特性?
"""
封装
"""

# 5. 以下代码体现 向对象的什么特性?
"""
封装
"""

# 6. 看代码写结果
"""
foo.func
None
"""

# 7. 看代码写结果
"""
foo.f0
base1.f3
base1.f1
"""

# 8. 看代码写结果
"""
foo.f2
foo.f1
base.f3
"""

# 9. 补充代码实现
"""
import re


class UserInfo(object):
    def __init__(self, name, pwd, email):
        self.name = name
        self.pwd = pwd
        self.email = email


def run():
    user_list = []
    while True:
        user = input("请输入用户名:")
        pwd = input("请输入密码:")
        email = input("请输入邮箱:")
        match_object = re.match("(\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*)", email, re.ASCII)
        if not match_object:
            print("邮箱格式输入错误，请重新输入！")
            continue
            
        user_object = UserInfo(user, pwd, email)
        user_list.append(user_object)
        if len(user_list) == 3:
            break
            
    for item in user_list:
        print(item.name, item.email)


if __name__ == '__main__':
    run()
"""


# 10. 补充代码实现

class User:
    def __init__(self, name, pwd):
        self.name = name
        self.pwd = pwd


class Account:
    def __init__(self):
        # 用户列表，数据格式：[user对象，user对象，user对象]
        self.user_list = []

    def login(self):
        """
        用户登录，输入用户名和密码然后去self.user_list中校验用户合法性
        :return:
        """
        print("用户登录")
        while True:
            user = input("请输入用户名(Q/q):")
            if user.upper() == 'Q':
                break
            pwd = input("请输入密码:")

            for user_object in self.user_list:
                if user == user_object.name and pwd == user_object.pwd:
                    print("登录成功")
                    break
            else:
                print("登录失败")

    def register(self):
        """
        用户注册，没注册一个用户就创建一个user对象，然后添加到self.user_list中，表示注册成功。
        :return:
        """
        print("用户注册")
        while True:
            user = input("请输入用户名(Q/q):")
            if user.upper() == 'Q':
                break
            pwd = input("请输入密码:")
            user_object = User(user, pwd)
            self.user_list.append(user_object)

    def run(self):
        """
        主程序
        :return:
        """

        method_dict = {
            "1": {"title": "登录", "method": self.login},
            "2": {"title": "注册", "method": self.register},
        }
        message = ";".join(["{}.{}".format(k, v['title']) for k, v in method_dict.items()])

        while True:
            print(message)
            choice = input("请选择功能(Q/q)：")
            if choice.upper() == 'Q':
                break
            info = method_dict.get(choice)
            if not info:
                print("选择错误，请重新选择")
                continue
            method = info['method']
            method()  # self.login()  /   self.register()


if __name__ == '__main__':
    obj = Account()
    obj.run()
