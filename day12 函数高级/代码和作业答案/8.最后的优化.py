import functools


def auth(func):
    @functools.wraps(func)  # inner.__name__ = func.__name__   inner.__doc__ = func.__doc__
    def inner(*args, **kwargs):
        """巴巴里吧"""
        res = func(*args, **kwargs)  # 执行原函数
        return res

    return inner


@auth
def admin():
    """这个是xxx的函数"""
    print(123)


@auth
def rbac():
    print("rbac")


# 函数名 + ()
# admin()
# print(admin.__name__)  # "admin"
# print(admin.__doc__)  # 这个是xxx的函数


print(admin.__name__)  # inner  / admin
print(admin.__doc__)  # 巴巴里吧 / 这个是xxx的函数

print(rbac.__name__)  # inner
print(rbac.__doc__)  # 巴巴里吧
