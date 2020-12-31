import random


def gen_random_num(max_count):
    counter = 0
    while counter < max_count:
        yield random.randint(1000, 9999)
        counter += 1


data_list = gen_random_num(3000000)
# 再使用时，去 data_list 中获取即可。
