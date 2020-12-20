# 第一题
"""
def char_count(text):
    count = 0
    for char in text:
        if char == 'a':
            count += 1
    return count


result = char_count("89alskdjf;auqkaaafasdfiojqln")
"""

# 第二题
"""
def judge_length(data):
    if len(data) > 5:
        return True
    return False


result = judge_length("武沛齐武沛齐")
print(result)
"""

# 第三题
"""
def get_bigger(num1, num2):
    if num1 > num2:
        return num1
    return num2


result = get_bigger(11, 22)
"""

# 第四题
"""
def write_file(name, gender, age, degree):
    data_list = [name, gender, age, degree]
    data = "*".join(data_list)
    with open('student_msg.txt', mode='a', encoding='utf-8') as file_object:
        file_object.write(data)


write_file("武沛齐", "男", "18", "博士")
"""

# 第五题
"""
import os


def select_content(file_path, key):
    # 补充代码【位置1】
    if not os.path.exists(file_path):
        return
    data_list = []
    with open(file_path, mode='r', encoding='utf-8') as file_object:
        for line in file_object:
            if key in line:
                data_list.append(line)
    return data_list


result = select_content("files/xxx.txt", "股票")
if result == None:
    print("文件不存在")
else:
    print(result)
"""

# 第六题
"""
def change_string(origin):
    # 补充代码，将字符串origin中中的敏感词替换为 **，最后将替换好的值返回。
    data_list = ["苍老师", "波多老师", "大桥"]
    for item in data_list:
        origin = origin.replace(item, "**")
    return origin


text = input("请输入内容：")
result = change_string(text)
print(result)
"""

# 第七题
"""
import hashlib
from openpyxl import load_workbook


def get_user_dict():
    user_dict = {}
    wb = load_workbook("files/user.xlsx")
    sheet = wb.worksheets[0]
    for row in sheet.rows:
        user_dict[row[1].value] = row[2].value
    return user_dict


def encrypt(origin):
    origin_bytes = origin.encode('utf-8')
    md5_object = hashlib.md5()
    md5_object.update(origin_bytes)
    return md5_object.hexdigest()


user = input("请输入用户名：")
pwd = input("请输入密码：")

encrypt_password = encrypt(pwd)

user_dict = get_user_dict()

db_password = user_dict.get(user)

if encrypt_password == db_password:
    print("登录成功")
else:
    print("登录失败")
"""
