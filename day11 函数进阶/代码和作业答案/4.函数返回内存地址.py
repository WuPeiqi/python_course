def func():
    data = 123123
    print(id(data))
    return data


v1 = func()
print(v1, id(v1))  # [11,22,33]

v2 = func()
print(v2, id(v1))  # [11,22,33]