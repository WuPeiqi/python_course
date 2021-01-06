import json
from decimal import Decimal
from datetime import datetime

data = [
    {"id": 1, "name": "武沛齐", "age": 18, 'size': Decimal("18.99"), 'ctime': datetime.now()},
    {"id": 2, "name": "alex", "age": 18, 'size': Decimal("9.99"), 'ctime': datetime.now()},
]


class MyJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if type(o) == Decimal:
            return str(o)  # "18.99"
        elif type(o) == datetime:
            # return str(o)
            return o.strftime("%Y-%M-%d")
        return super().default(o)


res = json.dumps(data, cls=MyJSONEncoder)
print(res)
