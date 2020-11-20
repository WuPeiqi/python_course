# 千万不要在循环的过程中，边循环获取列表的数据 边删除列表的数据。
"""
user_list = ["刘的话", "范德彪", "刘华强", '刘尼古拉斯赵四', "宋小宝", "刘能"]
for item in user_list:
    if item.startswith("刘"):
        user_list.remove(item)
print(user_list)  # ['范德彪', '刘尼古拉斯赵四', '宋小宝']
"""

# 倒着处理
"""
user_list = ["刘的话", "范德彪", "刘华强", '刘尼古拉斯赵四', "宋小宝", "刘能"]
for index in range(len(user_list) - 1, -1, -1):
    # 5 4 3 2 1 0
    item = user_list[index]
    if item.startswith("刘"):
        user_list.remove(item)
print(user_list)
"""