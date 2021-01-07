import string
import itertools

# 1.生成 0-9 A-z放到列表中。
"""
data = []
for i in string.digits:
    data.append(i)

for i in string.ascii_uppercase:
    data.append(i)

for i in string.ascii_lowercase:
    data.append(i)

data = []
for item in itertools.chain(string.digits, string.ascii_uppercase, string.ascii_lowercase):
    data.append(item)

data = [item for item in itertools.chain(string.digits, string.ascii_uppercase, string.ascii_lowercase)]
print(data)

data = list(itertools.chain(string.digits, string.ascii_uppercase, string.ascii_lowercase))
"""

MAP = list(itertools.chain(string.digits, string.ascii_uppercase, string.ascii_lowercase))
print(MAP)


def base62encode(num):
    total_count = len(MAP)  # 62

    position_value = []

    while num >= total_count:
        num, remain = divmod(num, total_count)
        position_value.insert(0, MAP[remain])

    position_value.insert(0, MAP[num])

    result = "".join(position_value)
    return result


v1 = base62encode(8)
v2 = base62encode(89)
v3 = base62encode(19889)
print(v1, v2, v3)
