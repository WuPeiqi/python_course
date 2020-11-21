info = {"age": 12, "status": True, "name": "武沛齐"}
if "agea" in info:

    del info["age"]
    data = info.pop("age")
    print(info)
    print(data)
else:
    print("键不足")
