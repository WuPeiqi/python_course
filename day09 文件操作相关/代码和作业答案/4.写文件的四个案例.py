# 案例1：用户注册
"""
user = input("请输入用户名：")
pwd = input("请输入密码：")
data = "{}-{}".format(user, pwd)
file_object = open("files/info.txt", mode='wt', encoding='utf-8')
file_object.write(data)
file_object.close()
"""

# 案例2：多用户注册
"""
# w写入文件，先清空文件；再在文件中写入内容。
file_object = open("files/info.txt", mode='wt', encoding='utf-8')
while True:
    user = input("请输入用户名：")
    if user.upper() == "Q":
        break
    pwd = input("请输入密码：")
    data = "{}-{}\n".format(user, pwd)

    file_object.write(data)
file_object.close()
"""