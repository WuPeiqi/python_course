import json
from flask import Flask

app = Flask(__name__)


def index():
    return "首页"


def users():
    data = [
        {"id": 1, "name": "武沛齐", "age": 18},
        {"id": 2, "name": "alex", "age": 18},
    ]
    return json.dumps(data)


app.add_url_rule('/index/', view_func=index, endpoint='index')
app.add_url_rule('/users/', view_func=users, endpoint='users')

if __name__ == '__main__':
    app.run()