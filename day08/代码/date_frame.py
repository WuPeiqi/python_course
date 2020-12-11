import random

total_poke_list = [("红桃", 1), ("黑桃", 2), ("大王", 15), ("小王", 14)]

# 随机生成一个数，当做索引。
index = random.randint(0, len(total_poke_list) - 1)
# 获取牌
print("抽到的牌为：", total_poke_list[index])
# 踢除这张牌
total_poke_list.pop(index)
