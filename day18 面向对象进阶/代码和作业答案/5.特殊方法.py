"""
info = dict()

# 字典对象支持    对象["xxx"]    对象["xxx"]=123  del 对象["xxx"]
info['k1'] = 123
info['k2'] = 456
print(info)
print(info['k1'])
del info['k1']
"""


class Foo(object):

    def __setitem__(self, key, value):
        print(key, value)

    def __getitem__(self, item):
        print(item)

    def __delitem__(self, key):
        print(key)


obj = Foo()

obj["xxx"] = 123  # 自动触发类中__setitem__

obj['ooo']  # 自动触发类中__getitem__

del obj['ooo']  # 自动触发类中__delitem__
