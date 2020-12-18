
welcome = "欢迎使用NB游戏".center(30, '*')
print(welcome)

user_count = 0
while True:
    count = input("请输入游戏人数：")
    if count.isdecimal():
        user_count = int(count)
        break
    else:
        print("输入格式错误，人数必须是数字。")


message = "{}人参加游戏NB游戏。".format(user_count)
print(message)


user_name_list = []

for i in range(1, user_count + 1):
    tips = "请输入玩家姓名（{}/{}）：".format(i, user_count)
    name = input(tips)
    user_name_list.append(name)

print(user_name_list)