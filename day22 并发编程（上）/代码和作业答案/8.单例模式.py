import threading
import time


class Singleton:
    instance = None
    lock = threading.RLock()

    def __init__(self, name):
        self.name = name

    def __new__(cls, *args, **kwargs):
        # 返回空对象
        if cls.instance:
            return cls.instance

        with cls.lock:
            if cls.instance:
                return cls.instance
            cls.instance = object.__new__(cls)
            return cls.instance


def task():
    obj = Singleton('x')
    print(obj)


for i in range(10):
    t = threading.Thread(target=task)
    t.start()

# 1000行代码。。。

obj = Singleton('x')
print(obj)