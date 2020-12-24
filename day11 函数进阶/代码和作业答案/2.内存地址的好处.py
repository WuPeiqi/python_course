
# 参数得是可变类型：list/dict/set & 在函数内部只能对内部元素进行修改。
def func(data):
    data.append(666)


data_list = [11, 22, 33]
# 函数
func(data_list)

print(data_list)
