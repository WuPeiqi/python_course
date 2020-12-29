from flask import Flask

app = Flask(__name__)


def auth(func):
    def inner(*args, **kwargs):
        # 判断用户是否已经登录，已登录继续网下走，未登录则返回登录页面。
        res = func(*args, **kwargs)  # 执行原函数
        return res

    return inner


@auth
def index():
    return "首页"


@auth
def info():
    return "用户中心"


@auth
def order():
    return "订单中心"


def login():
    return "登录页面"


app.add_url_rule("/index/", view_func=index)
app.add_url_rule("/info/", view_func=info)
app.add_url_rule("/order/", view_func=order)
app.add_url_rule("/login/", view_func=login)

app.run()
