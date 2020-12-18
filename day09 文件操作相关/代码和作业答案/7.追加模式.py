file_object = open('files/account.txt', mode='a')

while True:
    user = input("用户名：")
    if user.upper() == "Q":
        break
    pwd = input("密码：")
    data = "{}-{}\n".format(user, pwd)
    file_object.write(data)

file_object.close()
